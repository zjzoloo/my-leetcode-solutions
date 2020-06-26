# Author: Zoljargal Gantumur
# Runtime: 28 ms, faster than 75.80% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 35.23% of Python3 online submissions

class Solution:
    def numberOfSteps (self, num: int) -> int:
        step = 0
        while num!=0:
            if num%2==0:
                num = num//2
            else:
                num -= 1
            step += 1
        return step
