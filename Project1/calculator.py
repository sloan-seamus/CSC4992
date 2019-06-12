#!/usr/bin/env python3


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


print("\n\nCALCULATOR\n\n")
first = int(input(": "))
operator = input(": ")
second = int(input(": "))

switcher = {
    '+': add(first, second),
    '-': subtract(first, second),
    '/': divide(first, second),
    '*': multiply(first, second)
}

print("___________")
print(switcher.get(operator, "Invalid input."))
print("\n\n")


