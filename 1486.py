# Author: Zoljargal Gantumur
# Runtime: 28 ms, faster than 83.37% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1,n):
            ans = ans ^ (start + 2*i)
        return ans
