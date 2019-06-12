#!/usr/bin/env python3
import functools

factorial = functools.reduce(lambda x, y: x * y, list(range(1, 31)))

print("\n\nQuestion 3: \n")
print("30! = " + str(factorial))
print("\n\n")
