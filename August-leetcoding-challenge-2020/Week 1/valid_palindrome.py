# Author: Zoljargal Gantumur
# Runtime: 52 ms
# Memory Usage: 14.2 MB

# Given a string, determine if it is a palindrome, considering only alphanumeric characters 
# and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while not s[l].isalnum() and l < r: l += 1
            while not s[r].isalnum() and l < r: r -= 1
            if s[l] == s[r] or s[l].upper() == s[r].upper():
                l, r = l + 1, r - 1
            else:
                return False
        return True
