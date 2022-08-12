import math


def circle(r):
    return math.pi*r*r


r = float(input("r="))
print("Area=", circle(r), sep='')