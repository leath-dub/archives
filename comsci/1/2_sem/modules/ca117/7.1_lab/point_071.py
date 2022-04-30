class Point(object):

    def set_attributes(self, x, y):
        self.x = x
        self.y = y

    def print_attributes(self):
        print("x: {:.2f}".format(float(self.x)))
        print("y: {:.2f}".format(float(self.y)))

    def reflect(self):
        self.x *= -1
        self.y *= -1
