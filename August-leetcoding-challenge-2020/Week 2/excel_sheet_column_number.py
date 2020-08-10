# Runtime: 32 ms
# Memory Usage: 14 MB

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...


# Input: "A"
# Output: 1


# Input: "AB"
# Output: 28


# Input: "ZY"
# Output: 701

class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        ans = 0
        for i, char in enumerate(s):
            ans += (ord(char) - 64) * (26 ** i)
        return ans            

