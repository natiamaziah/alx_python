#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit = abs(number) % 10
neg_num=-last_digit
if last_digit > 5:
   if number<0:
      print("Last digit of" ,number, "is" ,neg_num, "and is less than 6 and not 0")
   else:   
    print("The string Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print("The string Last digit of", number, "is", last_digit, "and is 0")
elif 0<last_digit<6:
   if number<0:
     print("Last digit of", number, "is", neg_num, "and is less than 6 and not 0")
   else:    
    print("The string Last digit of", number, "is", last_digit, "and is less than 6 and not 0")

print()