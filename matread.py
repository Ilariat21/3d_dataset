import scipy.io
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def unique_point(nodes):
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

#path = "Datasets/ModelNet10/results/table_10b/table_0402.mat"
#path = "Datasets/ModelNet10/results/chair_10b/chair_0918.mat"
#path = "Datasets/ModelNet10/results/bed_10b/bed_0526.mat"
out_path = "bed_test_0393.obj"

def show_mat(path):

    mat = scipy.io.loadmat(path)
    nodes = mat["nodes"]
    print(nodes)

    nodes = unique_point(nodes)
    x = [nodes[i][0] for i in range(0, len(nodes))]
    y = [nodes[i][1] for i in range(0, len(nodes))]
    z = [nodes[i][2] for i in range(0, len(nodes))]

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(x, z, y, "gray")
    plt.show()


#show_mat(path)
for i in range(10, 27):
    print("Cube:", i)
    path = "Datasets/ModelNet10/results/rectangle_11a/res_rect_{}.mat".format(i)
    show_mat(path)

# python train.py --dataset 'ModelNet10' --category 'bed' --ckpt_model 'bed_10b' --batch_size 32 --node_num 14 --node_knn_k_1 3 --basis_num 10 --input_pc_num 1600 --surface_normal_len 0