#!/usr/bin/env python3

validElements = []

for i in range (0, 101, 5):
    if i % 2 != 0:
        validElements.append(i)
        print(i, end=',')


print("\n\nQuestion Three\n\n")
print(validElements)
print("\n\n")


"""
Test Cases:
    1. Run the program
    2. Verify that all elements listed are multiples of 5 but not multiples of 2
"""
