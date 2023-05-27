import os
import numpy as np
import random
import open3d as o3d

path = "rect1"
out_path = "rect2"
num_points = 2000


def check(path):
    if not os.path.exists(path):
        os.mkdir(path)


g = 0
filename = os.listdir(path)

for file_name in filename:
    mesh_new = o3d.io.read_triangle_mesh(f"{path}/{file_name}")

    f = open(f"{path}/{file_name}", "r")
    lines = f.readlines()
    vertices = []
    faces = []
    for line in lines:
        if line[0] == "v":
            # print(line)
            vertices.append(line)
        elif line[0] == "f":
            faces.append(line)
    x1, x2 = np.float64((np.min(np.asarray(mesh_new.vertices)[:, 0]))), np.float64(
        (np.max(np.asarray(mesh_new.vertices)[:, 0])))
    y1, y2 = np.float64((np.min(np.asarray(mesh_new.vertices)[:, 1]))), np.float64(
        (np.max(np.asarray(mesh_new.vertices)[:, 1])))
    z1, z2 = np.float64((np.max(np.asarray(mesh_new.vertices)[:, 2]))), np.float64(
        (np.min(np.asarray(mesh_new.vertices)[:, 2])))
    for i in range(num_points-len(vertices)):
        vertices.append(
            f"v {random.uniform(x1, x2)} {random.uniform(y1, y2)} {random.uniform(z1, z2)}\n")

    ff = open(f"{out_path}/res_rect_{g}.obj", "w")
    for v in vertices:
        ff.write(v)
    for face in faces:
        ff.write(face)

    print(f"res_rect_{g}.obj is done")
    g += 1

print("Finished!")
