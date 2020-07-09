# Author: Zoljargal Gantumur
# Runtime: 540 ms
# Memory Usage: 14.1 MB

#You are given a map in form of a two-dimensional integer grid where 1 represents 
#land and 0 represents water.

#Grid cells are connected horizontally/vertically (not diagonally). 
#The grid is completely surrounded by water, and there is exactly one island 
#(i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water 
# around the island). One cell is a square with side length 1. The grid is rectangular, 
# width and height don't exceed 100. Determine the perimeter of the island.
#Input:
#[[0,1,0,0],
# [1,1,1,0],
# [0,1,0,0],
# [1,1,0,0]]

#Output: 16

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        r,c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0: continue
                ans += 4
                if i>0: ans -= grid[i-1][j]
                if j>0: ans -= grid[i][j-1]
                if i<r-1: ans -= grid[i+1][j]
                if j<c-1: ans -= grid[i][j+1]
        return ans
