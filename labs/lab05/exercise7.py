import math 

user_input = input("Enter a number: ")
cube = float(user_input) ** 3

from math import sqrt, pow, sin

calculate = sqrt(float(user_input))
print("The square root of " + user_input + " is: " + str(calculate))
print("The square of " + user_input + " is: " + str(pow(float(user_input), 2)))
print("The cube of " + user_input + " is: " + str(pow(float(user_input), 3)))
print("The sine of " + user_input + " is: " + str(sin(float(user_input))))
