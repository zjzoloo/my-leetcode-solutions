# Runtime: 32 ms
# Memory Usage: 13.8 MB

# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.

# Input: k = 3, n = 7
# Output: [[1,2,4]]

# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def try_comb(comb, n, start):
            if k == len(comb):
                if n == 0: ans.append(comb.copy())
                return
            for i in range(start, 10):
                comb.append(i)
                try_comb(comb, n-i, i+1)
                comb.pop()
        try_comb([], n, 1)
        return ans
