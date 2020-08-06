# Author: ZOljargal Gantumur
# Runtime: 64 ms
# Memory Usage: 15.3 MB

# Given an array of numbers nums, in which exactly two elements appear only once and 
# all the other elements appear exactly twice. Find the two elements that appear only once.

# Example:
# Input:  [1,2,1,3,2,5]
# Output: [3,5]

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = reduce(xor, nums)
        diff &= -diff #retain last set bit
        ans = [0] * 2
        for x in nums:
            ans[bool(diff & x)] ^= x
        return ans
