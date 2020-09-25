# Given a list of non negative integers, arrange them such that they form the largest number.

# Input: [10,2]
# Output: "210"

# Input: [3,30,34,5,9]
# Output: "9534330"

class Key(str):
    def __lt__(x, y):
        return x+y > y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ''.join(sorted(map(str, nums), key=Key))
        return '0' if ans[0] == '0' else ans