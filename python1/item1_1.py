import math


def circle(r):
    return math.pi*(r**2)


r = float(input("r="))
print("Area=", circle(r), sep='')