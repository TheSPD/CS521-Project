import Tkinter
import random
import numpy as np
from time import time
from potentialReduction import potentialReduction as potRed

N = 100


def pixel(image, pos, color):
    """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
    r, g, b = color
    x, y = pos
    image.put("#%02x%02x%02x" % (r, g, b), (y, x))


def fillGrid(photo, grid, colors):
    """Fill the grid with the colors and grid matrix"""
    for i in range(N-1):
        for j in range(N-1):
            pixel(photo, (N-i, j), colors[grid[i][j] % len(colors)])

def getIter(i, j, N, Q):
    return potRed(np.array([[float(i) / N], [float(j) / N]], dtype=np.float64), Q, 1. / N)[1]

def plotGrid(Q, master):
    t0 = time()
    grid = [[getIter(i, j, N, Q) for i in range(1, N)] for j in range(1, N)]

    maxIter = max(grid[i][j] for i in range(N-1) for j in range(N-1))

    grid[0][0] = 0

    print 'Time taken... %f' % (time() - t0)

    colors = {i : (255 - ((255/maxIter) * i), 0, 0) for i in range(maxIter)}

    # grid = [[random.randrange(3) for i in range(N)] for j in range(N)]
    colors = {
        0: (255, 255, 255),
        1: (255, 0, 0),
        2: (0, 255, 0),
        3: (0, 0, 255),
        4: (255, 255, 0),
        5: (255, 0, 255),
        6: (0, 255, 255),
        7: (192, 192, 192),
        8: (128, 0, 0),
        9: (0, 128, 0),
        10: (0, 0, 128),
        11: (0, 128, 128),
        12: (128, 0, 128),
        13: (128, 128, 0),
        14: (128, 128, 128),
        15: (192, 0, 0),
        16: (0, 192, 0),
        17: (0, 0, 192)
    }

    root = Tkinter.Toplevel(master)
    root.wm_title("Grid")

    photo = Tkinter.PhotoImage(width=N, height=N)

    # Q = np.array([[20, 18], [18, 30]], dtype=np.float64)
    # print grid
    fillGrid(photo, grid, colors)


    label = Tkinter.Label(root, image=photo)
    label.grid()
    root.mainloop()

# Q = np.array([[20, 18], [18, 30]], dtype=np.float64)
# plotGrid(Q)