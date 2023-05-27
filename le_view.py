import open3d as o3d
import numpy as np

#path = "/home/uegook/Desktop/Lab/mylineset.obj"
path = "/home/uegook/Desktop/chair_testing2.obj"

def vis_line(path):
    with open(path, "r") as f:
        lines = f.readlines()

    all_elements = [l[:-1].split(" ") for l in lines]
    #print(all_elements)
    vs = [[0,0,0]]
    ls = []
    for line in all_elements:
        if line[0]=="v":
            vs.append(line[1:])
        elif line[0]=="l":
            ls.append(line[1:])

    vs = np.array(vs, dtype = np.float32)
    ls = np.array(ls, dtype = int)
    print(vs)
    lineset = o3d.t.geometry.LineSet(vs, ls)
    o3d.visualization.draw([lineset])

vis_line(path)
#for i in range(1090, 1094):
#    vis_line("{}{}_mesh_graph.obj".format(path, i))

