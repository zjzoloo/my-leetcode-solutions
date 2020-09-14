# Runtime: 116 ms
# Memory Usage: 17 MB

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # case when intervals is empty
        if len(intervals) == 0:
            return [newInterval]
        mergeIntervals = []
        start = newInterval[0]
        end = newInterval[1]
        overlap = False
        i = 0
        # case when end of newInterval is less than start of the first interval
        if end < intervals[0][0]:
            mergeIntervals.append(newInterval)
            overlap = True
        while i < len(intervals):
            # case when newInterval doesn't overlap with one interval from intervals
            if intervals[i][0] > end and not overlap:
                mergeIntervals.append(newInterval)
                overlap = True
            if intervals[i][0] <= start <= intervals[i][1] or intervals[i][0] <= end <= intervals[i][1] or (start < intervals[i][0] and end > intervals[i][1]):
                overlap = True
                startMerge = min(start, intervals[i][0])
                endMerge = max(end, intervals[i][1])
                
                i += 1
                while i < len(intervals):
                    if end < intervals[i][0]:
                        break
                    endMerge = max(end, intervals[i][1])
                    i += 1
                mergeIntervals.append([startMerge, endMerge])
                if i < len(intervals):
                    mergeIntervals.append(intervals[i])
            else:
                mergeIntervals.append(intervals[i])
            i += 1
        # case when start of newInterval is greater than end of the last interval
        if start > intervals[-1][1]:
            mergeIntervals.append(newInterval)
        
        return mergeIntervals
