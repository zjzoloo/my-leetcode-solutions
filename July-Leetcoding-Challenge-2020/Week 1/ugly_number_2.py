# Author: Zoljargal Gantumur
# Runtime: 1252 ms
# Memory Usage: 14 MB

#Write a program to find the n-th ugly number.
#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

#Example:

#Input: n = 10
#Output: 12
#Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n<=1:
            return n
        factors = [2,3,5]
        heap = factors + [1]
        heapq.heapify(heap)
        
        while n>1:
            uglyNum = heapq.heappop(heap)
            for factor in factors:
                nUglyNum = factor * uglyNum
                if nUglyNum not in heap:
                    heapq.heappush(heap, nUglyNum)
            n-=1
            
        return heapq.heappop(heap)
