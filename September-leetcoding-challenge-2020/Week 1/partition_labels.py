# Runtime: 36 ms
# Memory Usage: 13.6 MB

# A string S of lowercase English letters is given. We want to partition this string into as many
# parts as possible so that each letter appears in at most one part, and return a list of integers
# representing the size of these parts.


# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

# Note:
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        end_idx = [0]*26
        for i in range(len(S)):
            end_idx[ord(S[i]) - ord('a')] = i
        ans = []
        a, b = 0,0
        for i in range(len(S)):
            b = max(b, end_idx[ord(S[i]) - ord('a')])
            if i == b:
                ans.append(i-a+1)
                a = i+1
        return ans
