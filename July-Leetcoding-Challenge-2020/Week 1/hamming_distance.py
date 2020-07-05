# Author: Zoljargal Gantumur
# Runtime: 20ms
# Memory Usage: 13.9MB

#Input: x = 1, y = 4
#Output: 2
#Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

#The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x^y)[2:]
        count = 0
        for i in a:
            if i == '1':
                count+=1
        return count
