# Author: Zoljargal Gantumur
# Runtime: 112 ms, faster than 99.59% of Python3 online submissions
# Memory Usage: 14.5 MB, less than 95.10% of Python3 online submissions

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            low = 0 
            high = n-1
            res = -1
            while low <= high:
                mid = (low+high)//2
                if grid[i][mid] >= 0:
                    low = mid + 1
                elif grid[i][mid] < 0:
                    res = mid
                    high = mid - 1
            if res!=-1:
                count += (n-res)
        return count
