# Author: Zoljargal Gantumur
# Runtime: 56 ms, faster than 95.78% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n+i])
        return ans
