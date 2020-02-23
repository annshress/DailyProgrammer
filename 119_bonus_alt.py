"""
A STAR implementation
"""
import matplotlib.pyplot as plt


# SIZE = 5
# GRID = """S....
# WWWW.
# .....
# .WWWW
# ....E"""

SIZE = 8
GRID = """
S...W...
.WW.W.W.
.W..W.W.
......W.
WWWWWWW.
E...W...
WW..WWW.
........"""

grid = GRID.split("\n")

rstart = ''.join(grid).index('S') // SIZE
cstart = grid[rstart].index('S')
curr = [(rstart, cstart)]

rend = ''.join(grid).index('E') // SIZE
cend = grid[rend].index('E')
end = (rend, cend)

def heuristics(point):
  # closer point is to the end, smaller the weight
  return (end[0] - point[0])**2 + (end[1] - point[1])**2

visited = [
  # from: point
]

p_queue = [
  # point, from, heuristics
  (curr[0], curr[0], heuristics(curr[0])),
]

found = False

def push_queue(points, _from):
  for point in points:
    p_queue.append(
      (point, _from, heuristics(point))
    )
  p_queue.sort(key=lambda x: x[2])

plt.xlim((-1, SIZE))
plt.ylim((-1, SIZE))

while not found:
  if not p_queue:
    # queue is empty
    break
  ele = p_queue[0]

  coord = ele[0]
  neighs = [
    (coord[0], coord[1]+1),
    (coord[0], coord[1]-1),
    (coord[0]+1, coord[1]),
    (coord[0]-1, coord[1]),
  ]
  # not out of bounds
  neighs = filter(lambda x: 0 <= x[0] < SIZE and 0 <= x[1] < SIZE, neighs)
  # not wall
  neighs = filter(lambda x: grid[x[0]][x[1]] != "W", neighs)
  # not already visited
  neighs = filter(lambda x: x not in [list(d.values())[0] for d in visited], neighs)

  if grid[coord[0]][coord[1]] == "E":
    found = True

  visited.append({ele[1]: coord})
  #
  p_queue = p_queue[1:]

  # attach heuristics and push to queue, sort it afterwards
  push_queue(neighs, coord)


print(visited, end="\n\n")

# import time
for v in visited:
  f , t = list(v.items())[0]
  plt.plot([f[0], t[0]], [f[1], t[1]])
  plt.savefig('results/119_alt.png')
  # time.sleep(1)
