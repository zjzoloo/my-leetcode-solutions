# Runtime: 68 ms
# Memory Usage: 17.1 MB

# Given a collection of intervals, find the minimum number of intervals you need to remove to 
# make the rest of the intervals non-overlapping.


# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.


# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.


# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == []: return 0
        intervals.sort(key = lambda x:x[1])
        ans = 0
        end = intervals[0][0]
        for times in intervals:
            start = times[0]
            if start < end:
                ans += 1
            else:
                end = times[1]
        return ans
