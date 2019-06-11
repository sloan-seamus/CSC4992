#!/usr/bin/env python3


def convert(binary):
    return int(binary, 2)


print("\n\nQuestion Two\n\n")
num1 = input("Enter a binary number: ")

print("\nYou entered: ", num1)
print("In decimal: ", convert(num1))
print("\n\n")
