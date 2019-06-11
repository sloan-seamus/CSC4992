#!/usr/bin/env python3
import math

print("\n\nQuestion Four\n\n")
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))
print("\n")


if math.pow(b, 2) - (4 * a * c) <= 0:
    print("Error:\nsqrt({}^2 - 4({})({}))\nCannot be negative".format(b,a,c))
elif a == 0:
    print("a: {}\nValue for a cannot be 0".format(a))
else:
    positive_root = (-1 * b + math.sqrt(math.pow(b, 2) - (4 * a * c))) / 2
    minus_root = (-1 * b - math.sqrt(math.pow(b, 2) - (4 * a * c))) / 2
    print("\n{}x^2 + {}x + c: \n".format(a, b, c))
    print("x+ : {}\nx- : {}\n\n".format(positive_root, minus_root))

print("\n")

"""
Test Cases:
    Enter 0 for a
        Expected result: Program will throw an error saying that 0 is not allows
        
    Enter variables where 4ac is greater than b^2
        Expected result: Program will throw an error saying that this cannot be negative
        
    Enter variables where b^2 is greater than 4ac
        Expected result: Program will display the x+ and x- roots
"""
