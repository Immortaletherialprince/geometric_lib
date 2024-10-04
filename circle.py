import math


def area(r):
    '''на вход принимает радиус окружности ( r ) и выводит площадь данной окружности'''
    return math.pi * r * r


def perimeter(r):
    '''на вход принимает радиус окружности ( r ) и выводит длинну данной окружности'''
    return 2 * math.pi * r
print (perimeter(4))