# Runtime: 28 ms
# Memory Usage: 13.9 MB

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 5
# Output: false

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num 
 
"""
Number is positive.
Number is power of 2.
This power of 2 is even power.

First condition is trivial. For the second condition we can use x&(x-1) trick, 
which removes the last significant bit of binary representation, 
for example 11010 & 11001 = 11000. 
Number is power of two if it have only one significant bit, 
that is after this operation it must be equal to zero.

The last part is a bit tricky. Hopefully if reached this step, we already know, 
that number is a power of 2, so we have not a lot of options left: 1, 10, 100, 1000, ... 
How we can distinguish one half of them (odd powers) from another half? 
The trick is to use binary mask m = 1010101010101010101010101010101. 
For even powers of 2 we have for example m&100 = 100, if we use odd power, 
for example m&1000 = 0.

Complexity: both time and space is O(1).
"""
