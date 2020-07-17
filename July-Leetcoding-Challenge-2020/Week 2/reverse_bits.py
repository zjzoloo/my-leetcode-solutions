# Author: Zoljargal Gantumur
# Runtime: 44 ms
# Memory Usage: 14 MB

Reverse bits of a given 32 bits unsigned integer.

# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 represents the 
# unsigned integer 43261596, so return 964176192 which its binary representation is 
# 00111001011110000010100101000000.


# Input: 11111111111111111111111111111101
# Output: 10111111111111111111111111111111
# Explanation: The input binary string 11111111111111111111111111111101 represents the 
# unsigned integer 4294967293, so return 3221225471 which its binary representation is 
# 10111111111111111111111111111111.

class Solution:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
