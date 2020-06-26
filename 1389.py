# Author: Zoljargal Gantumur
# Runtime: 28 ms, faster than 90.13% of Python3 online submissions
# Memory Usage: 14 MB, less than 20.18% of Python3 online submissions

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, x in enumerate(index):
            ans.insert(x, nums[i])
        return ans
