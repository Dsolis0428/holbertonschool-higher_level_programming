#!/usr/bin/python3
def fizzbuzz():
    """function that prints the numbers from 1 to 100 separated by a space."""
    for number in range(0, 100):
        if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz ", end="")
    elif number % 3 == 0:
        print("Fizz ", end="")
    elif number % 5 == 0:
        print("buzz ", end="")
    else:
        print("{} ".format(number), end="")
