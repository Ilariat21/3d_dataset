import open3d as o3d
import numpy as np

# Purpose of the script:
# - Read an obj file containing lines
# - Visualize the lines using Open3D

# Specify the path to the obj file
path = "path-to-obj-file"

def vis_line(path):
    # Read the contents of the obj file
    with open(path, "r") as f:
        lines = f.readlines()

    all_elements = [l[:-1].split(" ") for l in lines]

    vs = [[0,0,0]]  # List to store vertices
    ls = []         # List to store lines

    # Parse the obj file contents
    for line in all_elements:
        if line[0] == "v":
            # Extract vertex coordinates and add to the list
            vs.append(line[1:])
        elif line[0] == "l":
            # Extract line indices and add to the list
            ls.append(line[1:])

    vs = np.array(vs, dtype=np.float32)
    ls = np.array(ls, dtype=int)

    # Create a LineSet object from the vertices and lines
    lineset = o3d.t.geometry.LineSet(vs, ls)

    # Visualize the LineSet using Open3D
    o3d.visualization.draw([lineset])

def main():
    vis_line(path)

if __name__ == "__main__":
    main()
