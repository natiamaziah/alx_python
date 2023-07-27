#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)

print("Last digit of {:d} is {1} and is greater than 5",number .format("number","num_str[-1]"))