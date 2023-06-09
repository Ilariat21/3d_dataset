import open3d as o3d
import os

# Indicate path to the point cloud
path = "Path-to-point-cloud"

def vis_mesh(path):
    # Check the file extension to determine the type of mesh
    if path[-3:] == "ply" or path[-3:] == "pcd" or path[-3:] == "off":
        # Read the point cloud data
        mesh = o3d.io.read_point_cloud(path)
    elif path[-3:] == "obj":
        # Read the triangle mesh data
        mesh = o3d.io.read_triangle_mesh(path)
    else:
        # Unsupported file format
        print("Unsupported file format.")
        return

    # Print the mesh object
    print(mesh)

    # Visualize the mesh using Open3D's visualization module
    o3d.visualization.draw_geometries([mesh])

def main():
    # Call the vis_mesh function with the specified path
    vis_mesh(path)

if __name__ == "__main__":
    # Execute the main function when the script is run directly
    main()
