
from enum import IntEnum


'''
Math
1. Calculate the final vector of how the robot travels after executing all instructions once - it consists of a change in position plus a change in direction.
2. The robot stays in the circle iff (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.
https://blog.csdn.net/fuxuemingzhu/article/details/92128721
'''

class Direction(IntEnum):
    N = 1
    W = 2
    S = 3
    E = 4
    def turn_left(self):
        if self == Direction.E:
            return Direction.N
        else:
            return Direction(self + 1)
    def turn_right(self):
        if self == Direction.N:
            return Direction.E
        else:
            return Direction(self - 1)

class Robot():
    def __init__(self):
        self.pos = (0, 0)
        self.direction = Direction.N
    def go_straight(self):
        if self.direction == Direction.N:
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif self.direction == Direction.W:
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif self.direction == Direction.S:
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif self.direction == Direction.E:
            self.pos = (self.pos[0] + 1, self.pos[1])
        else:
            raise Exception('Suck')
    def move(self, instruction):
        if instruction == 'L':
            self.direction = self.direction.turn_left()
        elif instruction == 'R':
            self.direction = self.direction.turn_right()
        elif instruction == 'G':
            self.go_straight()
        else:
            raise Exception('Suck')


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        robot = Robot()
        for instruction in instructions:
            robot.move(instruction)
        if robot.direction != Direction.N:
            return True
        if robot.pos == (0, 0):
            return True
        return False

instructions = "GGLLGG"
result = Solution().isRobotBounded(instructions)
assert result == True

instructions = "GG"
result = Solution().isRobotBounded(instructions)
assert result == False

instructions = "GL"
result = Solution().isRobotBounded(instructions)
assert result == True