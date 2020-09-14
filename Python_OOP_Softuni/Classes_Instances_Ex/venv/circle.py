class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        #pi * r ** 2
        area = self.pi * (self.radius**2)
        return area

    def get_circumference(self):
        #2pi * r
        circumference = (2 * self.pi) * self.radius
        return round(circumference, 2)

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
