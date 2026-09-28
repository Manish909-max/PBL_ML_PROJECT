"""
Code Execution Engine for Challenge Submissions
Safely executes user code and validates against test cases
"""
import subprocess
import json
import sys
import os
import tempfile
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class CodeExecutionError(Exception):
    """Custom exception for code execution errors"""
    pass


class CodeExecutor:
    """Executes code in different languages safely"""
    
    MAX_EXECUTION_TIME = 5  # seconds
    MAX_OUTPUT_SIZE = 10000  # characters
    
    @staticmethod
    def execute_python(code: str, test_cases: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Execute Python code with test cases
        test_cases: [{"input": "", "output": ""}, ...]
        """
        results = {
            "language": "python",
            "total_tests": len(test_cases),
            "passed_tests": 0,
            "test_results": [],
            "compilation_error": None,
            "runtime_error": None,
        }
        
        # Validate code syntax
        try:
            compile(code, '<string>', 'exec')
        except SyntaxError as e:
            results["compilation_error"] = f"Syntax Error: {str(e)}"
            return results
        
        for i, test_case in enumerate(test_cases):
            test_input = test_case.get('input', '')
            expected_output = test_case.get('output', '').strip()
            
            try:
                # Create a temporary file for the code
                with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                    # Write code with input handling
                    full_code = code
                    if test_input:
                        full_code = f"import io\nimport sys\nsys.stdin = io.StringIO('{test_input}')\n" + code
                    
                    f.write(full_code)
                    f.flush()
                    temp_file = f.name
                
                try:
                    # Execute with timeout
                    result = subprocess.run(
                        [sys.executable, temp_file],
                        capture_output=True,
                        text=True,
                        timeout=CodeExecutor.MAX_EXECUTION_TIME,
                        cwd=tempfile.gettempdir()
                    )
                    
                    output = result.stdout.strip()
                    
                    # Check if output matches expected
                    passed = output == expected_output
                    
                    results["test_results"].append({
                        "test_number": i + 1,
                        "input": test_input,
                        "expected_output": expected_output,
                        "actual_output": output[:CodeExecutor.MAX_OUTPUT_SIZE],
                        "passed": passed,
                        "error": result.stderr if result.returncode != 0 else None
                    })
                    
                    if passed:
                        results["passed_tests"] += 1
                    elif result.stderr:
                        results["runtime_error"] = result.stderr[:500]
                
                finally:
                    # Clean up temp file
                    try:
                        os.unlink(temp_file)
                    except:
                        pass
                        
            except subprocess.TimeoutExpired:
                results["runtime_error"] = "Execution timeout - code took too long"
                results["test_results"].append({
                    "test_number": i + 1,
                    "input": test_input,
                    "expected_output": expected_output,
                    "actual_output": None,
                    "passed": False,
                    "error": "Timeout"
                })
            except Exception as e:
                results["runtime_error"] = str(e)
                results["test_results"].append({
                    "test_number": i + 1,
                    "input": test_input,
                    "expected_output": expected_output,
                    "actual_output": None,
                    "passed": False,
                    "error": str(e)
                })
        
        return results
    
    @staticmethod
    def execute_javascript(code: str, test_cases: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Execute JavaScript code with test cases
        Requires Node.js to be installed
        """
        results = {
            "language": "javascript",
            "total_tests": len(test_cases),
            "passed_tests": 0,
            "test_results": [],
            "compilation_error": None,
            "runtime_error": None,
        }
        
        for i, test_case in enumerate(test_cases):
            test_input = test_case.get('input', '')
            expected_output = test_case.get('output', '').strip()
            
            try:
                # Create wrapper code with test case input
                wrapper = f"""
const input = '{test_input}';
let output = '';
const originalLog = console.log;
console.log = function(...args) {{
    output += args.join(' ') + '\\n';
}};
try {{
{chr(10).join('    ' + line for line in code.split(chr(10)))}
}} catch(e) {{
    console.log('ERROR: ' + e.message);
}}
console.log = originalLog;
process.stdout.write(output.trim());
"""
                
                with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
                    f.write(wrapper)
                    f.flush()
                    temp_file = f.name
                
                try:
                    result = subprocess.run(
                        ['node', temp_file],
                        capture_output=True,
                        text=True,
                        timeout=CodeExecutor.MAX_EXECUTION_TIME,
                        cwd=tempfile.gettempdir()
                    )
                    
                    output = result.stdout.strip()
                    passed = output == expected_output
                    
                    results["test_results"].append({
                        "test_number": i + 1,
                        "input": test_input,
                        "expected_output": expected_output,
                        "actual_output": output[:CodeExecutor.MAX_OUTPUT_SIZE],
                        "passed": passed,
                        "error": result.stderr if result.returncode != 0 else None
                    })
                    
                    if passed:
                        results["passed_tests"] += 1
                    
                except subprocess.TimeoutExpired:
                    results["runtime_error"] = "Execution timeout - code took too long"
                    results["test_results"].append({
                        "test_number": i + 1,
                        "input": test_input,
                        "expected_output": expected_output,
                        "actual_output": None,
                        "passed": False,
                        "error": "Timeout"
                    })
                finally:
                    try:
                        os.unlink(temp_file)
                    except:
                        pass
                        
            except Exception as e:
                results["runtime_error"] = str(e)
                results["test_results"].append({
                    "test_number": i + 1,
                    "input": test_input,
                    "expected_output": expected_output,
                    "actual_output": None,
                    "passed": False,
                    "error": str(e)
                })
        
        return results
    
    @staticmethod
    def execute(language: str, code: str, test_cases: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Main execution method supporting multiple languages
        """
        if not test_cases:
            return {"error": "No test cases provided"}
        
        if language == "python":
            return CodeExecutor.execute_python(code, test_cases)
        elif language == "javascript":
            return CodeExecutor.execute_javascript(code, test_cases)
        else:
            return {"error": f"Language '{language}' not yet supported"}
