import math
from array import *


class GetFunction(object):
    def __init__(self, val):
        self.name = functionList[val][0]
        self.formula = functionList[val][1]
        self.lowerLimit = functionList[val][2]
        self.upperLimit = functionList[val][3]
        self.dim = functionList[val][4]


def matyas(values):
    return .26 * (values[0]**2 + values[1]**2) - .48 * values[0] * values[1]


def easom(values):
    return -math.cos(values[0]) * math.cos(values[1]) * math.exp(
        -(values[0] - math.pi) ** 2 - (values[1] - math.pi) ** 2)


# name,function,lower limit,upper limit,dimension

functionList = [
    ["matyas", matyas, -10, 10, 2],
    ["easom", easom, -100, 100, 2]
]
