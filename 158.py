"""[4/16/2014] Challenge #158 [Intermediate] Part 1 - The ASCII Architect"""
import numpy as np

C = "**##--@@++"

design = (
    "j3f3e3e3d3d3c3cee3c3c3d3d3e3e3f3fjij3f3f3e3e3d3d3c3cee3c3c3d3d3e3e3fj"  # bridge
)
design = "3a3a3b3b3b3c3c3ciji3c3c3c3b3b3b3a3a"  # aeroplane

output = []
new = True

for char in design:
    if str.isdigit(char):
        output.append([*[" "] * int(char)])
        new = False
        continue
    if not new:
        output[-1].extend([x for x in C[: (ord(char) - 96)]])
        # print(*[x for x in C[: (ord(char) - 96)]], sep=" ")
        new = True
    else:
        output.append([x for x in C[: (ord(char) - 96)]])
        # print(*[x for x in C[: (ord(char) - 96)]], sep=" ")

height = len(max(output, key=lambda x: len(x)))
width = len(output)
mat = np.reshape([" "] * (width * height), (width, height))
for i in range(len(output)):
    mat[i] = output[i] + [" "] * (len(mat[i]) - len(output[i]))

for each in np.rot90(mat):
    print(*each, sep="")
