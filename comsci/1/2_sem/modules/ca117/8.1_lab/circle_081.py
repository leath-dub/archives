class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        new_instance = Point(
            (other.x - self.x) / 2 + self.x,
            (other.y - self.y) / 2 + self.y)
        return new_instance

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)

class Circle(object):

    def __init__(self, centre=None, radius=1):
        if centre is None:
            centre = Point()
        self.radius = radius
        self.centre = centre

    def __str__(self):
        return "Centre: {}\nRadius: {}".format(
            self.centre, self.radius)
