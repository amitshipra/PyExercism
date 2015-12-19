__author__ = 'dias'

import random as rand
import string

ALL_CHARS = string.ascii_uppercase


class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self, reset=False):
        return self.random_char(reset) + self.random_char(reset) + self.random_int(reset) + self.random_int(reset) + self.random_int(reset)

    def random_char(self, reset=False):
        return ALL_CHARS[rand.randint(0, 25)] if not reset else ALL_CHARS[rand.randint(0, 25)]

    def random_int(self, reset=False):
        return str(rand.randint(0, 9)) if not reset else str(rand.randint(0, 100) % 10)

    def reset(self):
        self.name = self.generate_name(True)
        return self.name


robot = Robot()

print(robot.name)


## Much elegant solution.
from random import sample, seed
from string import ascii_uppercase as AZ

nums = [str(c) for c in xrange(10)]

class Robot2:

    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        self.name = self.generate_name()

    def generate_name(self):
        seed() # seed from current time
        return ''.join(sample(AZ, 2) + sample(nums, 3))

robot2 = Robot2()

print(robot2.name)
