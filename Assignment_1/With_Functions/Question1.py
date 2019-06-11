#!/usr/bin/env python3


def average(numb1, numb2):
    summed = numb1 + numb2
    return summed / 2


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

print("\nMaximum: ", maximum)
print("Minimum: ", minimum)
averagestr = "Average: {}\n\n".format(average(num1, num2))
print(averagestr)