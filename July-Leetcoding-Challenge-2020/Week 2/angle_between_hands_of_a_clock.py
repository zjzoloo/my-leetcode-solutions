# Author: Zoljargal Gantumur
# Runtime: 48 ms
# Memory Usage: 13.9 MB

# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed 
# between the hour and the minute hand.

# Example 1:
# Input: hour = 12, minutes = 30
# Output: 165

# Example 2:
# Input: hour = 3, minutes = 30
# Output: 75

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans = abs((hour + minutes/60) * 30 - (minutes * 6))
        if ans>180:
            return 360-ans
        else:
            return ans
