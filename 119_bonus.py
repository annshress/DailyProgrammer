# SIZE = 5
# GRID = """S....
# WWWW.
# .....
# .WWWW
# ....E"""

SIZE = 8
GRID = """S...W...
.WW.W.W.
.W..W.W.
......W.
WWWWWWW.
E...W...
WW..WWW.
........"""

grid = GRID.split("\n")

visited = {
  # position: distance
  (0, 0): 0
}
visited_from = {
  # position: [from]
}

curr = [(0,0)]
directions = [(0,1), (0,-1), (1,0), (-1,0)]

distance = 0

# initial
new_curr = curr[:]

while new_curr:
  curr = new_curr[:]
  new_curr = []
  # distance
  distance += 1
  for coord in curr[:]:
    neighs = [
      (coord[0], coord[1]+1),
      (coord[0], coord[1]-1),
      (coord[0]+1, coord[1]),
      (coord[0]-1, coord[1]),
    ]
    # not out of bounds
    neighs = list(filter(lambda x: 0 <= x[0] < SIZE and 0 <= x[1] < SIZE, neighs))
    # not wall
    valid_n = list(filter(lambda x: grid[x[0]][x[1]] != "W", neighs))
    # not visisted, or distance is less
    unvisited_n = list(filter((lambda x: visited.get(x, distance + 1) > distance), valid_n))
    # store the visit information
    for each in unvisited_n:
      prev_distance = visited.get(each, distance + 1)
      if prev_distance >= distance:
        # update the new distance
        visited[each] = distance
        if prev_distance > distance:
          # replace all visited_from
          visited_from[each] = [coord]
        else:
          visited_from[each].append(coord)
    # remove the ends from the unvisited neighs
    new_curr += list(filter(lambda x: grid[x[0]][x[1]] != "E", unvisited_n))

print(visited, end="\n\n")
# visited_from = {k: v for k, v in visited_from.items()}
print(visited_from, end="\n\n")

import matplotlib.pyplot as plt
import matplotlib.lines as lines

plt.xlim((-1, SIZE))
plt.ylim((-1, SIZE))

for dest, src in visited_from.items():
  # print(dest, src)
  lines = [list(zip(*each)) for each in list(zip([dest]*len(src), src))]
  for line in lines:
    plt.plot(*line)
    plt.savefig('results/119.png')
    # plt.plot([0,1,4], [3,2,5])

