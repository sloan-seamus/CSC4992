#!/usr/bin/env python3
import random


def test_func(sample):
    """I'm not sure what I'm doing here"""
    print("This is inside a function, ", sample)


print("This is before the function")
name = input("Enter some text here: ")
print("You entered: ", name)

test_func(name)

number = random.randint(0, 10)
print(number)

quote = "You did it, {}!".format(name)

for i in list(range(5)):
    print("\nTrial #", i)
    guess = int(input("Enter a guess: "))
    print(guess == number)
    if guess == number:
        print(quote)
        break;
    else:
        print("Try again.")

print("\nThe correct number was: ", number)

