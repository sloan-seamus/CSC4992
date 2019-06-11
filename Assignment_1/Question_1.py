#!/usr/bin/env python3

print("\n\nQuestion One\n\n")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if num1 > num2:
    maximum = num1
    minimum = num2
elif num1 == num2:
    maximum = 0
    minimum = 0
else:
    maximum = num2
    minimum = num1

average = (num1 + num2) / 2

print("\nMaximum: {}\nMinimum: {}\nAverage: {}\n\n".format(maximum, minimum, average))

"""
Test Cases:
    Enter a large first number
    Enter a small second number
    Verify the maximum is the first number, the minimum is the second number
    Verify the average is correct
    
    Enter a small first number
    Enter a large second number
    Verify the maximum is the second number, the minimum is the first number
    Verify the average is correct
"""
