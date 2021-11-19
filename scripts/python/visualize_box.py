import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

pcd = np.load("/mnt/dataset/RoboSense/pcd/1608191068823792409.npy")
box = np.load("/mnt/dataset/RoboSense/box/0.npy")

print(pcd.shape)
print(box.shape)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

downsample = 20
# ax.scatter(pcd[::downsample, 0], pcd[::downsample, 1], pcd[::downsample, 2], marker=".")
ax.scatter(box[:, 0], box[:, 1], box[:, 2], marker=".")

idx = np.array([
  [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1], [1, 1, -1],
  [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1]]) / 2.0
for x, y, z, dx, dy, dz, h in box:
  cos = np.cos(h)
  sin = np.sin(h)
  pts = idx * [dx, dy, dz]
  pts = pts.dot([
    [cos, sin, 0],
    [-sin, cos, 0],
    [0, 0, 1]
  ])
  pts += [x, y, z]
  ax.plot(pts[:, 0], pts[:, 1], pts[:, 2])
  
plt.show()
