#!/usr/bin/env python3
import math


def quad_root_plus(a, b, c):
    result = -1 * b
    result = result + root(a, b, c)
    result = result / (2 * a)
    return result


def quad_root_minus(a, b, c):
    result = -1 * b
    result = result - root(a, b, c)
    result = result / (2 * a)
    return result


def root(a, b, c):
    inside = math.pow(b, 2)
    inside = inside - (4 * a * c)
    return math.sqrt(inside)


print("\n\nQuestion Three\n\n")
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))

print("x+ : ", str(quad_root_plus(a, b, c)))
print("x- : ", str(quad_root_minus(a, b, c)))
print("\n\n")

