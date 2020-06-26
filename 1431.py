# Author: Zoljargal Gantumur
# Runtime: 40 ms, faster than 53.95% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 43.85% of Python3 online submissions

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        asd = max(candies)
        for i in candies:
            if i + extraCandies >= asd:
                ans.append(True)
            else:
                ans.append(False)
        return ans
