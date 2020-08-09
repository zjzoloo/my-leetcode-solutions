# Runtime: 28 ms
# Memory Usage: 13.7 MB

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        c=[0]*(n+1)
        c[0]=1
        c[1]=1
        for i in range(2,n+1):
            c[i]=c[i-1]+c[i-2]
        return c[n]
