
import open3d as o3d
import os

path = "New_Dataset/filled_cube.off"

def vis_mesh(path):
    if path[-3:]=="ply" or path[-3:]=="pcd" or path[-3:]=="off":
        mesh = o3d.io.read_point_cloud(path)
    elif path[-3:]=="obj":
        mesh = o3d.io.read_triangle_mesh(path)
    
    print(mesh)

    o3d.visualization.draw_geometries([mesh])

vis_mesh(path)

