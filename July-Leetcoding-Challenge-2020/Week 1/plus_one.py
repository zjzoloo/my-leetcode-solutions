# Author: Zoljargal Gantumur
# Runtime: 48ms
# Memory Usage: 13.8 MB

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, 
# and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(0, len(digits)):
            idx = -1 + (-1 * i)
            val = digits[idx] + 1
            if val < 10:
                digits[idx] = val
                break
            if val == 10:
                digits[idx] = 0
                if i == (len(digits) - 1):
                    digits =  [1] + digits[:]
            
        return digits
