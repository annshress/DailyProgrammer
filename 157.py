"""[4/9/2014] Challenge #157 [Intermediate] Puzzle Cube Simulator
"""
import numpy as np

cube = np.reshape([""] * 125, (5, 5, 5))

cube[0, :, :] = np.reshape(["r"] * 25, (5, 5))  # F
cube[4, :, :] = np.reshape(["o"] * 25, (5, 5))  # B
cube[:, 0, :] = np.reshape(["y"] * 25, (5, 5))  # U
cube[:, 4, :] = np.reshape(["w"] * 25, (5, 5))  # D
cube[:, :, 4] = np.reshape(["g"] * 25, (5, 5))  # R
cube[:, :, 0] = np.reshape(["b"] * 25, (5, 5))  # L


def rotate(face, rot):
    if face == "F":
        cube[0, :, :] = np.rot90(cube[0, :, :], -1 * rot)
        cube[1, :, :] = np.rot90(cube[1, :, :], -1 * rot)
    if face == "B":
        cube[4, :, :] = np.rot90(cube[4, :, :], 1 * rot)
        cube[3, :, :] = np.rot90(cube[3, :, :], 1 * rot)
    if face == "U":
        cube[:, 0, :] = np.rot90(cube[:, 0, :], 1 * rot)
        cube[:, 1, :] = np.rot90(cube[:, 1, :], 1 * rot)
    if face == "D":
        cube[:, 3, :] = np.rot90(cube[:, 3, :], -1 * rot)
        cube[:, 4, :] = np.rot90(cube[:, 4, :], -1 * rot)
    if face == "L":
        cube[:, :, 0] = np.rot90(cube[:, :, 0], -1 * rot)
        cube[:, :, 1] = np.rot90(cube[:, :, 1], -1 * rot)
    if face == "R":
        cube[:, :, 3] = np.rot90(cube[:, :, 3], 1 * rot)
        cube[:, :, 4] = np.rot90(cube[:, :, 4], 1 * rot)


steps = "R U2 F2 D' F' U L' D2 U2 B' L R2 U2 D".split()
for step in steps:
    face = step[0]
    try:
        rot = step[1]
        if rot == "'":
            rotate(face, -1)
        if rot == "2":
            rotate(face, 1)
            rotate(face, 1)
    except IndexError:
        rotate(face, 1)

print(cube[0, :, :][1:4, 1:4])
