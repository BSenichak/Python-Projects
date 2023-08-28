"""
from math import pi, pow, trunc

def circleS(radius):
    s = pi * pow(radius, 2)
    return trunc(s)

print(circleS(int(input("Введіть радіус кола "))))
"""

from math import sqrt, pow

def pifagor(k1, k2):
    c = sqrt(pow(k1, 2) + pow(k2, 2))
    return c

a = int(input("a: "))
b = int(input("b: "))

result = pifagor(a, b)

print(result)