"""
    =========== Exercise 1 =============

    import the math module and use math.sqrt() on
    a user inputted variable.

    NOTE: you have the input converted to an int
    automatically using int(input()).
"""
# import math
# from math import sqrt

# user_input = int(input("Enter number for square root: "))
# print(sqrt(user_input))

"""
    =========== Exercise 2 =============

    import the sleep function from the time module as pause
    and run pause(5)
"""
# from time import sleep as pause

# print("Hello")

# pause(5)

# print("Hello")

"""
    =========== Exercise 3 (question) =============

    import the sleep function from the time module as pause.

    Write a function called pause() that takes an argument and
    prints it.

    Which pause() will be called, and why?
"""

from time import sleep as pause
def pause(num):
    print (num)

pause(4)