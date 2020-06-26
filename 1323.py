# Author: Zoljargal Gantumur
# Runtime: 16 ms, faster than 99.90% of Python3 online submissions
# Memory Usage: 14 MB, less than 14.51% of Python3 online submissions

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        i = s.find("6")
        if i == -1:
            return num
        return int(s[:i] + "9" + s[i +1 :])
    
