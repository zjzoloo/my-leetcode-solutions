# Author: Zoljargal Gantumur
# Runtime: 76 ms, faster than 6.48% of Python3 online submissions
# Memory Usage: 29.5 MB, less than 5.05% of Python3 online submissions

import numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = [int(i) for i in str(n)]
        return numpy.prod(lst) - sum(lst)
        
