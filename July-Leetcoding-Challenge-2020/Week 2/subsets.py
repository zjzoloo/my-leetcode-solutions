# Author: Zoljargal Gantumur
# Runtime: 28 ms
# Memory Usage: 14 MB

#Given a set of distinct integers, nums, return all possible subsets (the power set).
#Note: The solution set must not contain duplicate subsets.

#Input: nums = [1,2,3]
#Output:
#[
#  [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
#]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**len(nums), 2**(len(nums) + 1)):
            bitmask = bin(i)[3:]
            ans.append([nums[j] for j in range(len(nums)) if bitmask[j] == '1'])
        return ans
