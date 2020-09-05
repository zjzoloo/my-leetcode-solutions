# Runtime: 1396 ms
# Memory Usage: 16.4 MB

# Given an array of integers, find out whether there are two distinct indices i and j in the array
# such that the absolute difference between nums[i] and nums[j] is at most t and the absolute
# difference between i and j is at most k.

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true

# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false

from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False
        s = SortedList()
        for i, n in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            pos1 = bisect_left(s, n - t)
            pos2 =  bisect_right(s, n + t)
            if pos1 != pos2:
                return True
            s.add(n)
        return False
