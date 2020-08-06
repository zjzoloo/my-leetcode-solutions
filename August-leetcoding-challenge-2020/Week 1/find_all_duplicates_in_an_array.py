# Author: Zoljargal Gantumur
# Runtime: 400 ms
# Memory Usage: 21.1 MB

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums: 
            if nums[abs(num)-1] >= 0: 
                nums[abs(num)-1] = -nums[abs(num)-1] 
            else: 
                ans.append(abs(num))
        return ans
