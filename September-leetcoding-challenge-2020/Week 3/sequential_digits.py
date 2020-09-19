# Runtime: 32 ms
# Memory Usage: 13.8 MB

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# Input: low = 100, high = 300
# Output: [123,234]

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]

# Constraints:
# 10 <= low <= high <= 10^9

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l=[]
        for i in range(1,10):
            prev = i
            for j in range(i+1,10):
                prev = prev * 10 + j
                if  prev > 10**9:
                    break 
                l.append(prev)
        return sorted([ i for i in l if low <= i <= high ])
