import os
import numpy as np
import random
import open3d as o3d

# Purpose of the script: 
# - Generate modified obj files by adding random vertices to existing meshes
# - Save the modified obj files to a new directory

path = "input-folder"       # Directory path containing input obj files
out_path = "output-folder"  # Directory path to save modified obj files
num_points = 2000           # Total number of vertices in the resulting point cloud

def check(path):
    # Check if the directory exists, create it if not
    if not os.path.exists(path):
        os.mkdir(path)

def main():
    check(path)

    inc = 0  # Counter to keep track of modified obj files

    filename = os.listdir(path)

    for file_name in filename:
        mesh_new = o3d.io.read_triangle_mesh(f"{path}/{file_name}")

        f = open(f"{path}/{file_name}", "r")
        lines = f.readlines()
        vertices = []
        faces = []
        for line in lines:
            if line[0] == "v":
                # Append existing vertices to the list
                vertices.append(line)
            elif line[0] == "f":
                # Append existing faces to the list
                faces.append(line)

        # Extract the bounding box coordinates of the mesh
        x1, x2 = np.float64((np.min(np.asarray(mesh_new.vertices)[:, 0]))), np.float64(
            (np.max(np.asarray(mesh_new.vertices)[:, 0])))
        y1, y2 = np.float64((np.min(np.asarray(mesh_new.vertices)[:, 1]))), np.float64(
            (np.max(np.asarray(mesh_new.vertices)[:, 1])))
        z1, z2 = np.float64((np.max(np.asarray(mesh_new.vertices)[:, 2]))), np.float64(
            (np.min(np.asarray(mesh_new.vertices)[:, 2])))

        # Add random vertices to reach the desired total number of vertices
        while len(vertices) < num_points:
            vertices.append(
                f"v {random.uniform(x1, x2)} {random.uniform(y1, y2)} {random.uniform(z1, z2)}\n"
            )

        ff = open(f"{out_path}/res_rect_{inc}.obj", "w")
        for v in vertices:
            ff.write(v)
        for face in faces:
            ff.write(face)

        print(f"res_rect_{inc}.obj is done")
        inc += 1  # Increment the counter for the next modified obj file

    print("Finished!")

if __name__ == "__main__":
    main()
