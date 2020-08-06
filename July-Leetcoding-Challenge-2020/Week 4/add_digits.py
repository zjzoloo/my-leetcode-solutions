# Author: Zoljargal Gantumur
# Runtime: 32 ms
# Memory Usage: 14 MB

# Given a non-negative integer num, repeatedly add all its digits until the 
# result has only one digit. 
# Do it without any loop/recursion in O(1) runtime.

# Example:
# Input: 38
# Output: 2
 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#             Since 2 has only one digit, return it.

# 

class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
