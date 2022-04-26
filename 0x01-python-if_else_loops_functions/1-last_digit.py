#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number < 0:
    digit = number % -10
if digit > 5:
    memo = "and is greater than 5"
elif digit == 0:
    memo = "and is 0"
else:
    memo = "and is less than 6 and not 0"
print("Last digit of", number, "is", digit, "{}".format(memo))
