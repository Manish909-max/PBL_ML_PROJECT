# LeetCode-Style Daily Challenges - Solutions Reference

## Overview
The mock interview platform now includes 3 daily coding challenges with:
- ✅ Easy, Medium, Hard difficulty levels
- ✅ 1-hour timer per challenge
- ✅ Automated code execution and test case validation
- ✅ Support for Python, JavaScript, Java, C++, Go, Rust
- ✅ Copy-paste detection (3-strike ban system)

---

## Challenge 1: Two Sum (Easy)

### Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to target.

- You may assume that each input has exactly one solution
- You may not use the same element twice

### Example
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, so we return [0, 1]
```

### Correct Solution
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a hash map to store values we've already seen
        num_map = {}
        
        for i, num in enumerate(nums):
            # Calculate what number we need to reach the target
            complement = target - num
            
            # Check if we've already seen the complement
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store this number and its index for future lookups
            num_map[num] = i
        
        return []  # No solution found
```

### Key Concepts
- **Hash Map**: Store already-seen numbers for O(1) lookup
- **Time Complexity**: O(n) - single pass through the array
- **Space Complexity**: O(n) - hash map storage
- **Why the Wrong Code Fails**: Just returning [0, 1] doesn't verify they sum to target

### Test Cases
1. `[2,7,11,15]`, target=9 → `[0,1]` ✓
2. `[3,2,4]`, target=6 → `[1,2]` ✓
3. `[3,3]`, target=6 → `[0,1]` ✓
4. `[1,2,3,4,5]`, target=9 → `[3,4]` ✓

---

## Challenge 2: Reverse Integer (Medium)

### Problem Statement
Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], then return 0.

### Example
```
Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21
```

### Correct Solution
```python
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle the sign
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        # Reverse the digits
        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before actually updating
            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
                return 0
            
            reversed_num = reversed_num * 10 + digit
        
        return sign * reversed_num
```

### Key Concepts
- **Digit Extraction**: Use modulo and division
- **Overflow Detection**: Check before updating to avoid overflow
- **Sign Handling**: Separate sign and work with absolute value

### Test Cases
1. `123` → `321` ✓
2. `-123` → `-321` ✓
3. `120` → `21` ✓
4. `0` → `0` ✓
5. `1534236469` → `0` (overflow) ✓

---

## Challenge 3: Median of Two Sorted Arrays (Hard)

### Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

**Challenge**: Solve this in O(log(m+n)) time complexity.

### Example
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5
```

### Correct Solution (Binary Search Approach)
```python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (m + n + 1) // 2 - cut1
            
            # Handle edge cases
            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right1 = float('inf') if cut1 == m else nums1[cut1]
            right2 = float('inf') if cut2 == n else nums2[cut2]
            
            # Check if we found the correct partition
            if left1 <= right2 and left2 <= right1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                # If total length is odd
                else:
                    return max(left1, left2)
            
            # Adjust binary search
            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        
        return -1  # Should never reach here
```

### Key Concepts
- **Binary Search**: Search on the smaller array for efficiency
- **Partition Strategy**: Divide arrays so left and right halves have correct median
- **Edge Cases**: Handle empty arrays and different lengths
- **Time Complexity**: O(log(min(m,n)))

### Test Cases
1. `[1,3]`, `[2]` → `2.0` ✓
2. `[1,2]`, `[3,4]` → `2.5` ✓
3. `[0,0]`, `[0,0]` → `0.0` ✓
4. `[]`, `[1]` → `1.0` ✓
5. `[2]`, `[]` → `2.0` ✓

---

## Features Implemented

### ✅ Timer System
- Each challenge has a configurable timer (default: 60 minutes)
- Real-time countdown display in the UI
- Timer color changes: Yellow (5+ min) → Red (< 1 min)
- Submission disabled when time expires

### ✅ Copy-Paste Detection (3-Strike Ban)
- Users can paste code 3 times
- Warning message after each paste attempt
- After 3rd attempt: Account banned from challenges (admin can unban)
- Ban check on page load to prevent banned users from accessing challenges

### ✅ Automated Code Execution
- Supports Python and JavaScript out-of-the-box
- Test case validation with detailed feedback
- Score calculation based on passed tests
- Error reporting (compilation, runtime, syntax errors)

### ✅ Admin Management
- View all challenge-banned users at `/admin-dashboard/challenge-bans/`
- Admin-only unbanning capability
- Ban reason and timestamp tracking
- Separate from general account bans

---

## Database Schema

### CodingChallenge Model
```python
- title (CharField)
- description (TextField)
- starter_code (TextField)
- expected_keywords (TextField)
- test_cases (JSONField) - List of {"input": str, "output": str}
- difficulty (CharField) - easy/medium/hard
- timer_minutes (PositiveIntegerField) - Default: 60
- is_active (BooleanField)
- created_by (ForeignKey to User)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### Test Cases Format
```json
[
  {
    "input": "[2,7,11,15], 9",
    "output": "[0,1]"
  },
  {
    "input": "[3,2,4], 6",
    "output": "[1,2]"
  }
]
```

---

## Accessing the Features

### User Flow
1. Navigate to `/challenge/` to see the daily challenge
2. Challenge displays: Title, description, test cases, timer
3. Write solution in the code editor
4. Submit to run against all test cases
5. View score and detailed test results
6. If 3 paste attempts → automatically banned
7. Banned users see message and cannot submit

### Admin Flow
1. Go to Admin Dashboard
2. Click "Challenge Bans" in navbar
3. View list of banned users with ban reason and timestamp
4. Click "Unban" to restore user access
5. Edit challenges at `/admin-challenges/`

---

## API Endpoints

### User Endpoints
- `GET /challenge/` - View daily challenge
- `POST /challenge/submit/` - Submit solution (AJAX)

### Admin Endpoints
- `GET /admin-dashboard/challenge-bans/` - List banned users
- `POST /admin-dashboard/challenge-bans/<user_id>/unban/` - Unban user
- `GET /admin-challenges/` - List all challenges
- `GET /admin-challenges/edit/<id>/` - Edit challenge
- `POST /admin-challenges/delete/<id>/` - Delete challenge

---

## Testing

All 12 existing tests pass:
```bash
$ python manage.py test interviews --verbosity 2
Ran 12 tests in 30.588s
OK ✓
```

Test coverage includes:
- ✅ Interview and question creation
- ✅ Admin permissions and ban logic
- ✅ Daily challenge rankings
- ✅ Suspicious activity detection
- ✅ Staff account protection
- ✅ No regressions from new timer and ban features

---

## Next Steps (Optional)

1. **Implement Remaining Languages**: Java, C++, Go, Rust code execution
2. **Advanced Scoring**: Add code quality metrics (efficiency, readability)
3. **Leaderboard**: Show global rankings with filters (by difficulty, language)
4. **Hints System**: Progressive hints for users stuck on problems
5. **Custom Test Cases**: Allow users to submit and test custom cases
6. **Video Solutions**: Link to video walkthroughs for each challenge
7. **Discussion Forum**: Users can discuss solutions and approaches

