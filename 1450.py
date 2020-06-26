# Author: Zoljargal Gantumur
# Runtime: 36 ms, faster than 82.16% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 55.06% of Python3 online submissions

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(0, len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count+=1
        return count
