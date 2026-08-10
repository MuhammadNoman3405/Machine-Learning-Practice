import math
import sys
sys.set_int_max_str_digits(100000)
def factorial(number):
    print(f"The factorial of {number} is being calculated")
    result=math.factorial(number)
    print(f"factorial is: {result}")
    return result