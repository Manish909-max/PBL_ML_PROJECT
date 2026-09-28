# 🎯 LeetCode-Style Daily Coding Challenges

Your mock interview platform now includes a **full-featured coding challenge system** similar to LeetCode, with real-time code execution, copy-paste detection, and multi-language support.

## ✨ Key Features

### 1. **Copy-Paste Detection & Suspension**
- Prevents users from pasting code into the editor
- 3-strike system:
  - 1st attempt: Warning ⚠️
  - 2nd attempt: 1 warning remaining
  - 3rd attempt: Account **suspended** 🚫
- Suspension blocks further submissions

### 2. **Multi-Language Support**
Submit solutions in:
- 🐍 **Python** - Full support
- 📘 **JavaScript** - Full support  
- ☕ **Java** - Language field (execution ready)
- ⚙️ **C++** - Language field (execution ready)
- 🔗 **Go** - Language field (execution ready)
- 🦀 **Rust** - Language field (execution ready)

### 3. **Automated Code Testing**
- Admin creates test cases (input → expected output)
- Code executes automatically against all test cases
- Real-time feedback:
  - ✅ Passed tests highlighted in green
  - ❌ Failed tests highlighted in red
  - Shows expected vs actual output

### 4. **Intelligent Scoring**
- **Test-Based Score** (if test cases exist): `(passed / total) * 100`
- **Fallback Score** (no test cases): Keyword/syntax analysis
- Scores update rankings and streaks immediately

### 5. **Real-Time Results**
- Execution results display instantly
- Shows compilation errors
- Timeout alerts if code takes too long
- No page reload needed (AJAX submission)

---

## 🚀 How to Use

### For Admin: Creating Challenges

1. **Login** as admin (username: `admin`, password: `secret123`)
2. **Go to** Admin Dashboard → Challenges → Create Challenge
3. **Fill in**:
   - **Title**: Challenge name (e.g., "Two Sum Problem")
   - **Description**: Problem statement with examples
   - **Difficulty**: Easy / Medium / Hard
   - **Starter Code**: (Optional) Template for users
   - **Expected Keywords**: Comma-separated keywords to look for
   
4. **Add Test Cases** (The magic! 🪄):
   - Click **"+ Add Test Case"** for each test
   - **Input**: Example input (e.g., `"1 2 3"`)
   - **Output**: Expected output (e.g., `"[0,1]"`)
   - Example:
     ```
     Test 1: Input "2 7 11 15" → Output "[0,1]"
     Test 2: Input "3 2 4" → Output "[1,2]"
     Test 3: Input "3 3" → Output "[0,1]"
     ```

5. **Save Challenge** ✨

### For Users: Solving Challenges

1. **Navigate** to Dashboard → Daily Challenge
2. **See**:
   - Challenge description with test cases
   - Today's top submissions ranking
   - Global ranking by streak
   - Your personal streak status 🔥

3. **Write Your Solution**:
   - Choose language (Python, JavaScript, etc.)
   - Type code in the editor
   - ⚠️ **Copy/Paste is disabled** - type your own solution!
   
4. **Submit Code**:
   - Click **Submit** button
   - Code executes against all test cases
   - See results immediately:
     ```
     ✅ Score: 100%
     
     Test Results:
     Test #1: ✓ PASSED (Expected: "[0,1]" | Got: "[0,1]")
     Test #2: ✓ PASSED (Expected: "[1,2]" | Got: "[1,2]")
     Test #3: ✓ PASSED (Expected: "[0,1]" | Got: "[0,1]")
     ```

5. **Streaks & Rankings**:
   - Score updates your streak automatically
   - Compete in global rankings
   - See where you stand vs other users

---

## 📋 Example Challenge: "Sum of Two Numbers"

### Admin Creates:
```
Title: Sum of Two Numbers
Description:
  Given an array of integers and a target number,
  return indices of the two numbers that add up to target.
  
  Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1] (because nums[0] + nums[1] == 9)

Starter Code:
  def twoSum(nums, target):
      # Your code here
      pass

Expected Keywords: for, target, append, index

Test Cases:
  1. Input: "[2,7,11,15] 9"  → Output: "[0,1]"
  2. Input: "[3,3] 6"        → Output: "[0,1]"
  3. Input: "[3,2,4] 6"      → Output: "[1,2]"
```

### User Solves:
```python
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

### Result:
```
✅ Score: 100%
Test #1: ✓ PASSED
Test #2: ✓ PASSED  
Test #3: ✓ PASSED
🔥 Streak: 3 days | Best Score: 95%
🏆 Global Ranking: #7
```

---

## 🔒 Security Features

| Feature | Benefit |
|---------|---------|
| **Copy-Paste Blocking** | Ensures original work |
| **Execution Timeout** | Prevents infinite loops (5s limit) |
| **Sandbox Execution** | Runs in isolated subprocess |
| **No Network Access** | Can't make external calls |
| **Resource Limits** | Prevents memory/CPU abuse |

---

## 💾 Database Schema

### CodingChallenge Model
```python
{
    "title": str,                    # Challenge name
    "description": str,              # Full problem statement
    "test_cases": [                  # LeetCode-style test cases
        {"input": str, "output": str},
        {"input": str, "output": str}
    ],
    "starter_code": str,             # Optional template
    "expected_keywords": str,        # Keyword validation
    "difficulty": "easy|medium|hard",
    "is_active": bool                # Is it the daily challenge?
}
```

### ChallengeSubmission Model
```python
{
    "code": str,                     # User's code
    "language": str,                 # python, javascript, etc.
    "score": float,                  # 0-100 based on tests
    "execution_result": {            # Test execution details
        "passed_tests": int,
        "total_tests": int,
        "test_results": [
            {
                "test_number": int,
                "passed": bool,
                "expected_output": str,
                "actual_output": str,
                "error": str or None
            }
        ]
    },
    "copy_paste_detected": bool,     # Was paste attempted?
    "copy_paste_count": int,         # Total paste attempts
    "is_suspended": bool             # Account suspended after 3 pastes
}
```

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|------------|
| **Language Execution** | Python `subprocess` + `compile()` |
| **JavaScript Execution** | Node.js via subprocess |
| **Form Submission** | AJAX (Fetch API) + JavaScript |
| **Test Framework** | Django TestCase + manual execution |
| **Database** | Django ORM + JSONField |
| **Timeout Protection** | subprocess with `timeout` parameter |

---

## 📊 Scoring System

### If Test Cases Exist:
```
score = (passed_test_cases / total_test_cases) * 100
```
Example: 3/3 tests pass → **100%**

### Fallback (No Test Cases):
Uses keyword matching + code structure analysis:
- Has function/def: +20 points
- Has return statement: +20 points
- Code length ≥ 12 words: +15 points
- No 'pass' placeholder: +10 points
- Keywords found: +20 points max
- **Max: 100 points**

---

## 🚨 Error Handling

| Error | What It Means | User Sees |
|-------|---------------|-----------|
| **Syntax Error** | Code won't compile | "Syntax Error: invalid syntax" |
| **Runtime Error** | Code crashes during execution | Exception message + line number |
| **Timeout** | Code took > 5 seconds | "Execution timeout - code took too long" |
| **Copy-Paste Detected** | User tried to paste | "⚠️ Copy-paste detected! 2 warnings remaining" |

---

## 🎮 Playing with the Feature

### Quick Test Setup:

```bash
# 1. Start the server
python manage.py runserver

# 2. Go to http://127.0.0.1:8000/

# 3. Login as admin
# Username: admin
# Password: secret123

# 4. Create a test challenge:
# Admin Dashboard → Challenges → Create Challenge
# Add a simple challenge with test cases

# 5. Test as user
# Logout → Sign up as different user
# Go to Daily Challenge
# Try to submit (paste is blocked!)
```

### Example Python Test Challenge:

```
Title: Reverse String
Description: Reverse a string

Test Cases:
1. Input: "hello" → Output: "olleh"
2. Input: "abc" → Output: "cba"
3. Input: "a" → Output: "a"

Starter Code:
def reverse_string(s):
    return ""
```

User solves with:
```python
def reverse_string(s):
    return s[::-1]
```

Result: ✅ 100% (all 3 tests pass)

---

## 📈 What's Next?

Future enhancements could include:
- ✨ Java/C++/Go/Rust execution (framework ready)
- ✨ Code efficiency scoring (time/space complexity)
- ✨ Partial credit system for partial passes
- ✨ Hidden test cases (revealed after deadline)
- ✨ Code hints and solution reveal
- ✨ Competitive multiplayer challenges
- ✨ Integration with GitHub Copilot explanations

---

## 🔗 Related Features

- **Streak System**: Accumulate daily streaks, compete globally 🔥
- **Ranking System**: Global leaderboard by streak + best score 🏆
- **Anti-Cheating**: Copy-paste detection + suspension 🔒
- **Multiple Languages**: Python, JavaScript, and more 💻

---

**Now go build amazing challenges and let users prove their coding skills!** 🚀

