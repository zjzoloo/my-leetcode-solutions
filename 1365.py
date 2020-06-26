# Author: Zoljargal Gantumur
# Runtime: 344 ms, faster than 34.10% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 91.38% of Python3 online submissions

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sorted(nums).index(i) for i in nums]
