import open3d as o3d
import copy
import numpy as np
import os

# Purpose:
#        This function takes an input mesh file and creates a rectangular prism mesh by resizing and combining
#        square meshes in three dimensions. The resulting mesh is saved as an OBJ file in the specified output
#        directory. Additionally, if the visualization parameter is set to True, the generated mesh is displayed.


path = "rects/unit_square.obj"  # Input path
out_path = "rect1"              # Output path
filename = "good"               # Name for the output mesh

# Define the scaling factors
a = 0.5
b = 0.7
c = 0.3


def rect(path, out_path, a, b, c, filename, visualization=False):
    """
    Create a rectangular prism mesh from a given input mesh file.

    Args:
        path (str): Path to the input mesh file (PLY, PCD, or OBJ format).
        out_path (str): Output directory path to save the generated rectangular prism mesh.
        a (float): Scaling factor along the x-axis.
        b (float): Scaling factor along the y-axis.
        c (float): Scaling factor along the z-axis.
        namee (str): Name of the output rectangular prism mesh file.
        visualization (bool, optional): If True, visualize the generated mesh. Default is False.
    """

    if path[-3:] == "ply" or path[-3:] == "pcd" or path[-3:] == "off":
        mesh = o3d.io.read_point_cloud(path)
    elif path[-3:] == "obj":
        mesh = o3d.io.read_triangle_mesh(path)

    # Creating square meshes in 3 dimensions
    mesh_xy = copy.deepcopy(mesh)
    mesh_yz = copy.deepcopy(mesh).rotate(mesh.get_rotation_matrix_from_xyz((0, np.pi / 2, 0)), center=(0, 0, 0))
    mesh_xz = copy.deepcopy(mesh).rotate(mesh.get_rotation_matrix_from_xyz((-np.pi / 2, 0, 0)), center=(0, 0, 0))

    # Resizing all planes
    mesh_xy.vertices = o3d.utility.Vector3dVector(np.asarray(mesh_xy.vertices) * np.array([a, b, c]))
    mesh_yz.vertices = o3d.utility.Vector3dVector(np.asarray(mesh_yz.vertices) * np.array([a, b, c]))
    mesh_xz.vertices = o3d.utility.Vector3dVector(np.asarray(mesh_xz.vertices) * np.array([a, b, c]))

    # Creating second planes of the same normal direction
    mesh_xy2 = copy.deepcopy(mesh_xy).translate((0, 0, np.float64((np.min(np.asarray(mesh_yz.vertices)[:, 2])))))
    mesh_yz2 = copy.deepcopy(mesh_yz).translate((np.float64((np.max(np.asarray(mesh_xy.vertices)[:, 0]))), 0, 0))
    mesh_xz2 = copy.deepcopy(mesh_xz).translate((0, np.float64((np.max(np.asarray(mesh_xy.vertices)[:, 1]))), 0))

    # Combining all meshes into one
    mesh_new = mesh_xz + mesh_xy + mesh_yz + mesh_xy2 + mesh_xz2 + mesh_yz2

    # Set visualization to True if needed, default=False
    if visualization:
        o3d.visualization.draw_geometries([mesh_new])

    # Save output mesh
    o3d.io.write_triangle_mesh(f"{out_path}/rectangle_{filename}.obj", mesh_new)
    print(f"rectangle_{filename}.obj is done")


def main():
    if not os.path.exists(out_path):
        os.mkdir(out_path)

    rect(path, out_path, a, b, c, filename)


if __name__ == "__main__":
    main()
