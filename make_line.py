import numpy as np
from scipy.spatial import cKDTree
import scipy.io
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import open3d as o3d

# point_cloud = np.load("Datasets/ModelNet10/test_data_npy/chair/chair_0918.npy")
# point_cloud = np.load("Datasets/ModelNet10/test_data_npy/bed/bed_0526.npy")
point_cloud = np.load("Datasets/ModelNet10/test_data_npy/table/table_0402.npy")

# keypoints = "Datasets/ModelNet10/results/chair_10a/chair_0918.mat"
# keypoints = "Datasets/ModelNet10/results/bed_10b/bed_0526.mat"
keypoints = "Datasets/ModelNet10/results/table_10b/table_0402.mat"


def unique_point(nodes):
    x = [nodes[i][0] for i in range(0, len(nodes))]
    y = [nodes[i][1] for i in range(0, len(nodes))]
    z = [nodes[i][2] for i in range(0, len(nodes))]
    nodes_new = [[x[0], y[0], z[0]]]
    for i in range(1, len(x)):
        g = 0
        for j in range(len(nodes_new)):
            d = ((x[i] - x[j]) ** 2 + (y[i] - y[j])
                 ** 2 + (z[i] - z[j]) ** 2) ** 0.5
            if abs(d) < 0.2:
                g = 1
        if g == 0:
            nodes_new.append([x[i], y[i], z[i]])
    return nodes_new


point_cloud = point_cloud[:, :3]
mat = scipy.io.loadmat(keypoints)
nodes = mat["nodes"]

# Define the distance threshold
d = 0.1

nodes = unique_point(nodes)
# Construct a KD-tree from the point cloud
tree = cKDTree(point_cloud)

ls = []

# Loop through each pair of keypoints
for i in range(len(nodes)-1):
    for j in range(i+1, len(nodes)):
        p1 = nodes[i]
        p2 = nodes[j]
        p01 = [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2]
        p02 = [(3*p1[0]+p2[0])/4, (3*p1[1]+p2[1])/4, (3*p1[2]+p2[2])/4]
        p03 = [(p1[0]+3*p2[0])/4, (p1[1]+3*p2[1])/4, (p1[2]+3*p2[2])/4]

    # Compute the nearest neighbor distances for the line segment
        dist1, idx = tree.query(p01, k=1)
        dist2, idx = tree.query(p02, k=1)
        dist3, idx = tree.query(p03, k=1)
        if dist1 <= d and dist2 <= d and dist3 <= d:
            ls.append([i, j])


vs = np.array(nodes, dtype=np.float32)
ls = np.array(ls, dtype=int)

vs = np.asarray(vs).astype('float32')
ls = np.asarray(ls).astype('int')
lineset = o3d.t.geometry.LineSet(vs, ls)
o3d.visualization.draw([lineset])
