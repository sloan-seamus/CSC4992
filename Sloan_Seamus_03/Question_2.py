#!/usr/bin/env python3

celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = map(lambda c: (c * 9 / 5) + 32, celsius)

converted = set(fahrenheit)
print("\n\nQuestion 2:\n")
print("Celsius: " + str(sorted(celsius)))
print("Fahrenheit: " + str(sorted(converted)))
print("\n\n")