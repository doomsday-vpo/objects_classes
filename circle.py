# Create a class Circle. In the __init__ method, the circle should only receive one parameter - its diameter.
# Create a class attribute called __pi that is equal to 3.14. The class should also have the following methods:
# •	calculate_circumference() - returns the circumference of the circle
# •	calculate_area() - returns the area of the circle
# •	calculate_area_of_sector(angle) - gives the central angle in degrees, returns the area that fills the sector
# Notes: Search the formulas on the internet. Name your methods and variables exactly as in the description! Submit only the class.
#     Test your class before submitting it!

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def calculate_circumference(self):
        return round(2 * Circle.pi * self.radius, 2)

    def calculate_area(self):
        return round(Circle.pi * (self.radius ** 2), 2)

    def calculate_area_of_sector(self, angle):
        return round((angle / 360) * Circle.pi * (self.radius ** 2), 2)


