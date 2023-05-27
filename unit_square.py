import os
import numpy as np

path = "rects"
filename = "unit_square.obj"
x1 = 0
x2 = 0.9
st = 0.07


def check(path):
    if not os.path.exists(path):
        os.mkdir(path)


def unit_square(x1, x2, st, path, filename):
    obj = open(f"{path}/{filename}", "w")

    x, y = np.meshgrid(np.arange(x1, x2 + st, st), np.arange(x1, x2 + st, st))

    vertices = np.column_stack((x.ravel(), y.ravel()))

    faces = []
    mx = int(abs((x2 + st - x1) / st)) + 1

    for i in range(mx):
        for j in range(mx):
            if not int((i + 1) % mx) == 0 and not int((j + 1) % mx) == 0:
                faces.append([mx * j + i + 1, mx * j + i + 2, mx * (j + 1) + i + 1])
                faces.append(
                    [mx * j + i + 2, mx * (j + 1) + i + 1, mx * (j + 1) + i + 2]
                )

    for v in vertices:
        obj.write(f"v {round(v[0],2)} {round(v[1],2)} {x1} \n")

    for f in faces:
        obj.write(f"f {f[0]} {f[1]} {f[2]}\n")


check(path)
unit_square(x1, x2, st, path, filename)
