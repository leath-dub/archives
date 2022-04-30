class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p2):
        p2 = eval(p2.__str__())
        (x1, y1) = (self.x, self.y)
        (x2, y2) = (p2[0], p2[1])
        return ((y2 - y1)**2 + (x2 - x1)**2)**(0.5)

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)
