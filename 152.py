"""[14/04/2014] Challenge #152 [Hard] Minimum Spanning Tree"""
# Reverse-delete algorithm

import numpy as np

# INPUT = """8
# -1,11,9,6,-1,-1,-1,-1
# 11,-1,-1,5,7,-1,-1,-1
# 9,-1,-1,12,-1,6,-1,-1
# 6,5,12,-1,4,3,7,-1
# -1,7,-1,4,-1,-1,2,-1
# -1,-1,6,3,-1,-1,8,10
# -1,-1,-1,7,2,8,-1,6
# -1,-1,-1,-1,-1,10,6,-1"""

INPUT = """10
-1,29,-1,-1,18,39,-1,-1,-1,-1
29,-1,37,-1,-1,20,-1,-1,-1,-1
-1,37,-1,28,-1,43,47,-1,-1,-1
-1,-1,28,-1,-1,-1,35,-1,-1,-1
18,-1,-1,-1,-1,31,-1,36,-1,-1
39,20,43,-1,31,-1,34,-1,33,-1
-1,-1,47,35,-1,34,-1,-1,-1,22
-1,-1,-1,-1,36,-1,-1,-1,14,-1
-1,-1,-1,-1,-1,33,-1,14,-1,23
-1,-1,-1,-1,-1,-1,22,-1,23,-1"""

arr = []
weights = []


def reformat_array():
    # responsible for keeping only the half below the diagonal since our input is non-directional
    for i in range(int(count)):
        for j in range(int(count)):
            if i < j:
                arr[i][j] = -1


def format_edges(l):
    retval = list(zip(list(l[0]), list(l[1])))
    return retval
    # return set([tuple(sorted(each)) for each in retval])


def get_edge(weight):
    # find the first edge with the given edge
    l = np.where(arr == str(weight))
    return format_edges(l)


def get_connected_edges():
    # get all connected edges
    l = np.where(arr != "-1")
    return format_edges(l)


def get_neighbors(src, dest, visited):
    # for given src, dest find neighbors that has not been visited yet
    all_edges = get_connected_edges()
    # get all neighbors of the source
    if len(visited) <= 1:
        # for the first check, we want to ignore the direct link between the src-dest vertices
        return {
            item
            for each in all_edges
            for item in each
            if src in each
            if item not in visited
        } - set([src, dest])
    return {
        item
        for each in all_edges
        for item in each
        if src in each
        if item not in visited
    }


def check_path_exists(src, dest, visited, neighbors=None):
    # visited to prevent visited neighbors from being added to neighbors list
    # neighbors keeps track of vertices required to visit
    if not neighbors:
        neighbors = []
    neighbors += get_neighbors(src, dest, visited)
    if dest in neighbors:
        return True

    if not neighbors:
        return
    new_src = neighbors.pop()
    visited.append(new_src)
    return check_path_exists(new_src, dest, visited, neighbors)


def delete_edge(edge):
    arr[edge[0]][edge[1]] = -1


def reverse_delete_algo():
    for w in weights:
        try:
            to_delete = get_edge(w)[0]
        except IndexError:
            # caused by duplicate edges due to non-directionality
            pass
        if check_path_exists(to_delete[0], to_delete[1], visited=[to_delete[0]]):
            delete_edge(to_delete)
    print("complete...")


if __name__ == "__main__":
    count, *rows = INPUT.split("\n")
    for length in range(int(count)):
        row = rows[length]
        # arr.append(row.split(",")[:length+1])
        arr.append(row.split(","))

        for x in row.split(","):
            if int(x) > -1:
                weights.append(int(x))
    arr = np.array(arr)
    reformat_array()
    weights.sort(reverse=1)

    print("Default graph edges: ", get_connected_edges())
    reverse_delete_algo()
    print("Minimal graph edges: ", get_connected_edges())
    edges = get_connected_edges()
    print("Formally...")
    s = 0
    for edge in edges:
        s += int(arr[edge[0]][edge[1]])
        for vert in edge:
            print(chr(vert + 97).upper(), end="")
        print(end=", ")
    print(s)
