import math
def calculate_circumference(radius):
    circumfrence = 2 * math.pl * radius
    return circumfrence
radius = float(input("enter the radius of the circle:"))
print("the circumference of a circle with radius {radius} is:"
"{calculate_circumference(radius)}")