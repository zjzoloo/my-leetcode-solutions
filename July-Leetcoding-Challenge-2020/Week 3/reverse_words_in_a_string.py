# Author: Zoljargal Gatnumur
# Runtime: 40 ms
# Memory Usage: 14.3 MB

# Given an input string, reverse the string word by word.

# Example 1:
# Input: "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
