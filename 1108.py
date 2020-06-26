# Author: Zoljargal Gantumur
# Runtime: 28 ms, faster than 73.30% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 71.99% of Python3 online submissions

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split('.'))
        
