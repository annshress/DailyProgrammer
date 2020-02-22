"""
Challenge #138 [Intermediate] Overlapping Circles
"""
import math
import matplotlib.pyplot as plt
import matplotlib


class Coordinate(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    @property
    def val(self):
        return (self.x, self.y)


INPUT = "-0.5 0 0.5 0"
# given
RADIUS = 1

if __name__ == "__main__":
    x1, y1, x2, y2 = INPUT.split(" ")
    p1 = Coordinate(x1, y1)
    p2 = Coordinate(x2, y2)
    distance = p1.distance(p2)

    apothem = distance / 2

    if apothem > 1.0:
        area = 2 * math.pi * RADIUS ** 2
    else:
        # get the central angle
        radian = 2 * math.acos(apothem)

        # area of the segment
        overlapped_area = (RADIUS ** 2 / 2) * (radian - math.sin(radian))

        # area of the venn diagram
        area = 2 * (math.pi * RADIUS ** 2 - overlapped_area)

    # matplotlib.patches.Circle(p2.val, RADIUS, color="g")
    circle1 = plt.Circle(p1.val, RADIUS, color="r", fill=False)
    circle2 = plt.Circle(p2.val, RADIUS, color="blue", fill=False)
    fig, ax = plt.subplots()
    fig = plt.gcf()
    # ax = fig.gca()
    # ax.add_artist(circle1)
    ax.set_xlim((-3, 3))
    ax.set_ylim((-3, 3))
    fig.suptitle(f"Area: {area}")

    ax.add_artist(circle1)
    ax.add_artist(circle2)
    fig.savefig("results/138.png")

