#!/usr/bin/env python3


"""

 Use map and lambda functions only to convert the
 following list of temperatures from Celsius to
 Fahrenheit:
 [39.2, 36.5, 37.3, 37.8]

"""

celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = map(lambda x: (x * 9 / 5) + 32, celsius)

fahrenheit = set(fahrenheit)

print("\nQuestion Two:\n\n")
print("Celsius: {}".format(celsius), sep='\t', end='\n')
print("Fahrenheit: {}".format(fahrenheit, sep='\t', end='\n'))
print("\n\n")
