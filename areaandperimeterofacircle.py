import math
class circle:
    def __init__(self, radius):
        self.raidus = radius
    def area(self):
        return math.pi * self.raidus ** 2
r = float(input("enter radius of a circle: "))
c = circle(r)
print("area:", c.area())
print("perimeter:", c.perimeter())