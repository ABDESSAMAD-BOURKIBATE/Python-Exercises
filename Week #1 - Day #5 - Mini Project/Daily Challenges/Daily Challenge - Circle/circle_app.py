import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either radius or diameter.")
    
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area():.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("Can only add Circle to Circle.")

    def __gt__(self, other):
        return self.radius > other.radius if isinstance(other, Circle) else NotImplemented

    def __lt__(self, other):
        return self.radius < other.radius if isinstance(other, Circle) else NotImplemented

    def __eq__(self, other):
        return self.radius == other.radius if isinstance(other, Circle) else NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other


# Helper functions

def add_circle(circles):
    choice = input("Create by radius or diameter? (r/d): ").lower()
    if choice == "r":
        r = float(input("Enter radius: "))
        c = Circle(radius=r)
    elif choice == "d":
        d = float(input("Enter diameter: "))
        c = Circle(diameter=d)
    else:
        print("❌ Invalid choice.")
        return
    circles.append(c)
    print(f"✅ Circle added: {c}")

def list_circles(circles):
    if not circles:
        print("No circles yet.")
        return
    print("\n--- Circles List ---")
    for idx, c in enumerate(circles, start=1):
        print(f"{idx}. {c}")
    print("--------------------\n")

def add_two_circles(circles):
    if len(circles) < 2:
        print("❌ Need at least two circles to add.")
        return
    list_circles(circles)
    i = int(input("Select first circle number: ")) - 1
    j = int(input("Select second circle number: ")) - 1
    if i >= len(circles) or j >= len(circles) or i < 0 or j < 0:
        print("❌ Invalid selection.")
        return
    new_circle = circles[i] + circles[j]
    circles.append(new_circle)
    print(f"✅ New circle from addition: {new_circle}")

def compare_circles(circles):
    if len(circles) < 2:
        print("❌ Need at least two circles to compare.")
        return
    list_circles(circles)
    i = int(input("Select first circle number: ")) - 1
    j = int(input("Select second circle number: ")) - 1
    if i >= len(circles) or j >= len(circles) or i < 0 or j < 0:
        print("❌ Invalid selection.")
        return
    c1, c2 = circles[i], circles[j]
    print(f"{c1} > {c2} ? {c1 > c2}")
    print(f"{c1} < {c2} ? {c1 < c2}")
    print(f"{c1} == {c2} ? {c1 == c2}")

def sort_circles(circles):
    if not circles:
        print("No circles to sort.")
        return
    sorted_circles = sorted(circles)
    print("\n--- Sorted Circles by Radius ---")
    for c in sorted_circles:
        print(c)
    print("-------------------------------\n")
    return sorted_circles

def draw_circles(circles):
    if not circles:
        print("No circles to draw.")
        return
    t = turtle.Turtle()
    t.speed(1)
    t.penup()
    for idx, c in enumerate(circles):
        t.goto(0, -c.radius)
        t.pendown()
        t.circle(c.radius)
        t.penup()
        t.goto(0, 0)
    turtle.done()


# Main menu

def main():
    circles = []
    while True:
        print("\n--- Circle Manager ---")
        print("1. Add a new circle")
        print("2. List all circles")
        print("3. Add two circles")
        print("4. Compare two circles")
        print("5. Sort circles")
        print("6. Draw circles")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_circle(circles)
        elif choice == "2":
            list_circles(circles)
        elif choice == "3":
            add_two_circles(circles)
        elif choice == "4":
            compare_circles(circles)
        elif choice == "5":
            sorted_circles = sort_circles(circles)
        elif choice == "6":
            if 'sorted_circles' in locals():
                draw_circles(sorted_circles)
            else:
                draw_circles(circles)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
