# Runtime: 156 ms
# Memory Usage: 14 MB

# Given a non-empty string check if it can be constructed by taking a substring of it and appending
# multiple copies of the substring together. You may assume the given string consists of lowercase
# English letters only and its length will not exceed 10000.


# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.

# Input: "aba"
# Output: False

# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        lps = [0]*n
        for i in range(1, n):
            j = lps[i-1]
            while j > 0 and s[i] != s[j]: j = lps[j-1]
            if s[i] == s[j]: j += 1
            lps[i] = j
        l = lps[n-1]
        return l != 0 and (l % (n-l) == 0)
