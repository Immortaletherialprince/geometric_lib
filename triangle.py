import math

def area(a, b, c):
    return math.sqrt((a + b + c) / 2 * (b + c - a) / 2 * (a + c - b) / 2 * (a + b - c) / 2)


def perimeter(a, b, c):
    return a + b + c
