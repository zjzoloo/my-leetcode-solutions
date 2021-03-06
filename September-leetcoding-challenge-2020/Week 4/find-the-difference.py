# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Find the letter that was added in t.

# Input:
# s = "abcd"
# t = "abcde"
# Output:
# e

# Explanation:
# 'e' is the letter that was added.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char = 0
        for char_s in s: char ^= ord(char_s)
        for char_t in t: char ^= ord(char_t)
        return chr(char)