""" Methods and classes objects """
class Circle:
    # Class Attribute
    pi = 3.1416
    def __init__(self, radius = 1):
        self.radius = radius

    # Methods
    def get_are(self):
        area_circle = self.radius ** 2 * self.pi
        print(f'The circle area is: {area_circle: .2f}')   


my_circle = Circle()
my_circle.radius = 12.18

my_circle.get_are()