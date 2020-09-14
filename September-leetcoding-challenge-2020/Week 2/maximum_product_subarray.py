# Runtime: 100 ms
# Memory Usage: 14.9 MB

#Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        v = nums[::-1]
        
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            v[i] *= v[i-1] or 1
        return max(nums+v)
