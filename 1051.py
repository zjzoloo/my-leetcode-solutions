# Author: Zoljargal Gantumur
# Runtime: 36 ms, faster than 60.90% of Python3 online submissions
# Memory Usage: 14 MB, less than 19.71% of Python3 online submissions

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        asd = heights.copy()
        asd.sort()
        ans = 0
        for i in range(len(asd)):
            if asd[i] != heights[i]:
                ans+=1
        return ans
