import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def definition(self):
        print("A circle is a round plane figure whose boundary (the circumference) consists of points equidistant from a fixed point (the center).")

c = Circle(5)
print("Radius:", c.radius)
print("Perimeter:", round(c.perimeter(), 2))
print("Area:", round(c.area(), 2))
c.definition()
