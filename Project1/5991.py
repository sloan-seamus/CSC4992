def divisibleByFive(number):
    if number % 5 == 0:
        return True
    else:
        return False


def divisibleByThree(number):
    if number % 3 == 0:
        return True
    else:
        return False


for number in range (1, 101):
    if divisibleByThree(number) and divisibleByFive(number):
        print("FizzBuzz")
    elif divisibleByThree(number):
        print("Fizz")
    elif divisibleByFive(number):
        print("Buzz")
    else:
        print(number)
