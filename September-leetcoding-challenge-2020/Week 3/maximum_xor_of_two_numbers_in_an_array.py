# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

# Follow up: Could you do this in O(n) runtime?

# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.

# Input: nums = [0]
# Output: 0

# Input: nums = [2,4]
# Output: 6

# Input: nums = [8,10,2]
# Output: 10

# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in range(31, -1, -1):
            guess = ans | (1 << i)
            pref = {guess & n for n in nums}
            if any((guess ^ pre) in pref for pre in pref):
                ans = guess
        return ans
