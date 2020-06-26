# Author: Zoljargal Gantumur
# Runtime: 28 ms, faster than 73.49% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 69.80% of Python3 online submissions

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        c = 0
        for i in range(len(s)):
            if(s[i]=='R'):
                ans+=1
            else:
                ans-=1
            if ans==0:
                c+=1
        return c
