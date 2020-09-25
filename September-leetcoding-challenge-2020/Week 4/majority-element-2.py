# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Input: [3,2,3]
# Output: [3]

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in set(nums):
            if nums.count(i) > n/3:
                ans.append(i)
        return ans