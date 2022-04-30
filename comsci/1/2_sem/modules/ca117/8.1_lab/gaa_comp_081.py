class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return "{} goal(s) and {} point(s)".format(
            self.goals, self.points)

    def __eq__(self, other):
        return ((3 * self.goals + self.points) == (
            3 * other.goals + other.points))

    def __lt__(self, other):
        return ((3 * self.goals + self.points) < (
            3 * other.goals + other.points))

    def __le__(self, other):
        return ((3 * self.goals + self.points) <= (
            3 * other.goals + other.points))

    def __gt__(self, other):
        return ((3 * self.goals + self.points) > (
            3 * other.goals + other.points))

    def __ge__(self, other):
        return ((3 * self.goals + self.points) >= (
            3 * other.goals + other.points))
