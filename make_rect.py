import open3d as o3d
import copy
import numpy as np
import os


path = "rects/unit_square.obj"
out_path = "rect1"
x1, x2, st = -0.5, 0.5, 0.1


a = 0.5
b = 0.7
c = 0.3
namee = "good"


def check(path):
    if not os.path.exists(path):
        os.mkdir(path)


def rect(path, out_path, a, b, c, namee, visualization=False):
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
    # Creating second planes of same normal direction
    mesh_xy2 = copy.deepcopy(mesh_xy).translate((0, 0, np.float64((np.min(np.asarray(mesh_yz.vertices)[:, 2])))))
    mesh_yz2 = copy.deepcopy(mesh_yz).translate((np.float64((np.max(np.asarray(mesh_xy.vertices)[:, 0]))), 0, 0))
    mesh_xz2 = copy.deepcopy(mesh_xz).translate((0, np.float64((np.max(np.asarray(mesh_xy.vertices)[:, 1]))), 0))
    # Combining all meshes into one
    mesh_new = mesh_xz + mesh_xy + mesh_yz + mesh_xy2 + mesh_xz2 + mesh_yz2
    # set visualization to True if needed, default=False
    if visualization:
        o3d.visualization.draw_geometries([mesh_new])
    # Save output mesh
    o3d.io.write_triangle_mesh(f"{out_path}/rectangle_{namee}.obj", mesh_new)
    print(f"rect_{namee}.obj is done")


check(out_path)
rect(path, out_path, a, b, c, namee)

# g = 0
# for i in range(1, 11):
#    for j in range(1, 11):
#        for k in range(1, 11):
#            a = i*0.08
#            b = j*0.08
#            c = k*0.08
#            rect(path, out_path, a, b, c, g)
#            g += 1
# print("Finished!")
