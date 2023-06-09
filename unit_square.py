import os
import numpy as np


path = "folder-name"          # Directory path where the obj file will be saved
filename = "unit_square.obj"  # The name of the obj file to be created
x1 = 0                        # Starting value of the unit square vertices
x2 = 0.9                      # Ending value of the unit square vertices
st = 0.07                     # Step size of the unit square vertices


def check(path):
    # Check if the directory exists, create it if not
    if not os.path.exists(path):
        os.mkdir(path)


def unit_square(x1, x2, st, path, filename):
    # Open the obj file for writing
    obj = open(f"{path}/{filename}", "w")

    # Generate x and y coordinates using np.meshgrid
    x, y = np.meshgrid(np.arange(x1, x2 + st, st), np.arange(x1, x2 + st, st))

    # Stack x and y coordinates to form vertices
    vertices = np.column_stack((x.ravel(), y.ravel()))

    faces = []
    mx = int(abs((x2 + st - x1) / st)) + 1

    # Generate the faces for the unit square
    for i in range(mx):
        for j in range(mx):
            if not int((i + 1) % mx) == 0 and not int((j + 1) % mx) == 0:
                faces.append([mx * j + i + 1, mx * j + i + 2, mx * (j + 1) + i + 1])
                faces.append(
                    [mx * j + i + 2, mx * (j + 1) + i + 1, mx * (j + 1) + i + 2]
                )

    # Write the vertices to the obj file
    for v in vertices:
        obj.write(f"v {round(v[0],2)} {round(v[1],2)} {x1} \n")

    # Write the faces to the obj file
    for f in faces:
        obj.write(f"f {f[0]} {f[1]} {f[2]}\n")


def main():
    # Create the directory if it doesn't exist
    check(path)

    # Generate the unit square and save it as an obj file
    unit_square(x1, x2, st, path, filename)


if __name__ == "__main__":
    # Execute the main function when the script is run directly
    main()
