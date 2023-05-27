import scipy.io
import numpy as np
import matplotlib.pyplot as plt

#data = np.load("Datasets/ModelNet10/test_data_npy/bed/bed_0526.npy")
data = np.load("Datasets/ModelNet10/test_data_npy/rectangle/res_rect_24.npy")
#data = np.load("Datasets/ModelNet10/test_data_npy/chair/chair_0918.npy")

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

show_input(data)
#for i in range(1, 21):
#    print("cube:", i)
#    data = np.load("Datasets/ModelNet10/test_data_npy/cube/filled_cube_{}.npy".format(i))
#    show_input(data)