import math
number = float(input("enter a number to find the square root: "))
if number < 0:
    print("square root of negative number is not real (use complex number).")
else:
    sqrt_value = math.sqrt(number)
    print("square root of {number} is {sqrt_value:.6f}")