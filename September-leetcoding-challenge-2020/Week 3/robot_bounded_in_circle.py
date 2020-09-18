# Runtime: 28 ms
# Memory Usage: 13.6 MB

# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.


# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

# Input: "GG"
# Output: false
# Explanation: 
# The robot moves north indefinitely.

# Input: "GL"
# Output: true
# Explanation: 
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        N, E, S, W = 0, 1, 2, 3
        x, y, dir = 0, 0, N
        for _  in range(4):
            for i in instructions:
                if i == 'R': dir = (dir + 1) % 4
                elif i=='L': dir = (4 + dir - 1) % 4
                else:
                    if dir == N: y += 1
                    elif dir == E: x += 1
                    elif dir == S: y -= 1
                    else: x -= 1
        return (x==0 and y==0) 
