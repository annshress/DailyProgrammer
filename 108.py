"""
Challenge #108 [Intermediate] (Minesweeper Generation)
"""
from random import shuffle

HEIGHT: int = 15
WIDTH: int = 15
MINES: int = 20

grid = [[0 for o in range(WIDTH + 2)] for p in range(HEIGHT + 2)]

locations = [i for i in range(HEIGHT * WIDTH)]
shuffle(locations)

for location in locations[:MINES]:
    x, y = (location // WIDTH) + 1, (location % HEIGHT) + 1
    # add the mine count in the surrouding
    grid[x][y] = "M"
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (grid[x + i][y + j] == "M") or (not i and not j):
                continue
            grid[i + x][j + y] += 1

for x in grid:
    print(*[y for y in x], sep=" ")
