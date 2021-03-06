# Runtime: 80 ms
# Memory Usage: 14.4 MB

# Given an array A of non-negative integers, return an array consisting of all the even elements of
# A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans_even = []
        ans_odd = []
        for i in A:
            if i%2==0:
                ans_even.append(i)
            else:
                ans_odd.append(i)
        return ans_even + ans_odd
