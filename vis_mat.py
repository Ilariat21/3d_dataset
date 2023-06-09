import scipy.io
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Purpose of the script:
# - Load a MATLAB file containing point cloud data
# - Remove duplicate points from the point cloud
# - Visualize the point cloud in 3D using matplotlib

# Path to the MATLAB file
path = "path-to-mat-file"
    
def unique_point(nodes):
    """
    Function to remove duplicate points from the given list of nodes.
    """
    x = [nodes[i][0] for i in range(0, len(nodes))]
    y = [nodes[i][1] for i in range(0, len(nodes))]
    z = [nodes[i][2] for i in range(0, len(nodes))]
    nodes_new = [[x[0], y[0], z[0]]]
    for i in range(1, len(x)):
        g = 0
        for j in range(len(nodes_new)):
            d = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2) ** 0.5
            if abs(d) < 0.1:
                g = 1
        if g == 0:
            nodes_new.append([x[i], y[i], z[i]])

    return nodes_new


def show_mat(path):
    """
    Load the MATLAB file containing point cloud data, remove duplicate points, and visualize the point cloud.
    """
    # Load the MATLAB file
    mat = scipy.io.loadmat(path)
    nodes = mat["nodes"]

    # Remove duplicate points from the point cloud
    nodes = unique_point(nodes)
    x = [nodes[i][0] for i in range(0, len(nodes))]
    y = [nodes[i][1] for i in range(0, len(nodes))]
    z = [nodes[i][2] for i in range(0, len(nodes))]

    # Create a 3D scatter plot of the point cloud
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(x, z, y, "gray")
    plt.show()


def main():
    # Call the function to visualize the MATLAB file
    show_mat(path)


if __name__ == "__main__":
    main()
