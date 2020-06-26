# Author: Zoljargal Gantumur
# Runtime: 40 ms, faster than 80.98% of Python3 online submissions
# Memory Usage: 14.8 MB, less than 63.02% of Python3 online submissions


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i%3==0:
                ans.append("FizzBuzz") if i%5==0 else ans.append("Fizz")
            elif i%5==0:
                ans.append("FizzBuzz") if i%3==0 else ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
                
