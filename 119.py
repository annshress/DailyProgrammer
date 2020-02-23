"""
Challenge #119 [Intermediate] Find the shortest path
"""

VISITED = set()

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.prev = None
        # self.distance = 0

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def visit(self):
        VISITED.add((self.x, self.y))

    def is_wall(self):
        return GRID[self.x][self.y] == "W"
    
    def is_end(self):
        return GRID[self.x][self.y] == "E"

    @classmethod
    def has_end(cls, points):
        return any([point.is_end() for point in points])

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def get_neighbors(self):
        in_range = list(filter(lambda neighbor: 0 <= neighbor.x < MAX and 0 <= neighbor.y < MAX, 
                               [self + each for each in [LEFT, RIGHT, UP, DOWN]]))
        unvisited = filter(lambda each: (each.x, each.y) not in VISITED, in_range)
        not_wall = list(filter(lambda x: not x.is_wall(), unvisited))
        [each.visit() for each in not_wall]
        return not_wall

    @classmethod
    def calculate(cls, curr):
        # if not curr:
        #     curr = cls(0, 0)
        new_n = []
        for c in curr:
            new_n += c.get_neighbors()
        if cls.has_end(new_n):
            raise ValueError
        return new_n


LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
UP = Point(0, 1)
DOWN = Point(0, -1)

grid = """S...W...
.WW.W.W.
.W..W.W.
......W.
WWWWWWW.
E...W...
WW..WWW.
........"""

GRID = [line for line in grid.split("\n")]
MAX = len(GRID)

if __name__ == "__main__":
    step = 0
    curr = [Point(0, 0)]
    try:
        while 1:
            step += 1
            curr = Point.calculate(curr)
            if not curr:
                print("None")
                break
    except ValueError:
        print(step)
