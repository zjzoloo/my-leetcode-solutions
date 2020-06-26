# Author: Zoljargal Gantumur
# Runtime: 36 ms, faster than 92.99% of Python3 online submissions
# Memory Usage: 14.1 MB, less than 33.33% of Python3 online submissions

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        a = 0
        for i in nums:
            a+=i
            ans.append(a)
        return ans
