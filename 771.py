# Author: Zoljargal Gantumur
# Runtime: 36 ms, faster than 30.58% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 86.53% of Python3 online submissions

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in range(len(S)):
            for j in range(len(J)):
                if S[i] == J[j]:
                    count += 1
        return count

