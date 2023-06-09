import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Purpose of the script:
# - Load and visualizea point cloud data file of npy format
# - This script is used for input data from category-specific keypoints network

# Specify the path to the point cloud data file
data_file = "path-to-npy-file"

def show_input(data):
    # Extract the x, y, and z coordinates from the data
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]

    # Create a 3D scatter plot of the point cloud
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter(x, z, y)
    plt.show()

def main():
    # Load the point cloud data from the file
    data = np.load(data_file)

    # Visualize the point cloud
    show_input(data)

if __name__ == "__main__":
    main()
