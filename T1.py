# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.gca(projection='3d')

P = np.matrix([[1],
              [1],
              [0],
              [1]])

rotateYPos45Matrix = np.matrix([
                         [math.cos(math.pi / 4), 0, math.sin(math.pi / 4), 0],
                         [0, 1, 0, 0],
                         [-1 * math.sin(math.pi / 4), 0, math.cos(math.pi / 4), 0],
                         [0, 0, 0, 1]]
                         )
rotateXPos30Matrix = np.matrix([[1, 0, 0, 0],
                         [0, math.cos(math.pi / 6), -1 * math.sin(math.pi / 6), 0],
                         [0, math.sin(math.pi / 6), math.cos(math.pi / 6), 0],
                         [0, 0, 0, 1]]
                         )
rotateYNeg45Matrix = np.matrix([
                         [math.cos(math.pi * -1 / 4), 0, math.sin(math.pi * -1 / 4), 0],
                         [0, 1, 0, 0],
                         [-1 * math.sin(math.pi * -1 / 4), 0, math.cos(math.pi * -1 / 4), 0],
                         [0, 0, 0, 1]]
                         )
P1 = rotateYNeg45Matrix * rotateXPos30Matrix * rotateYPos45Matrix * P
print(P1)

# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 10)
y = x
z = 0
ax.plot(x, y, z, zdir='z', label='OA(1, 0, 1)')
ax.scatter(P[0, 0], P[1, 0], P[2, 0], zdir='y', label='P(1, 1, 0)')
ax.scatter(P1[0, 0], P1[1, 0], P1[2, 0], zdir='y', label='P1')
ax.scatter(0, 0, 0, zdir='y', label='O(0, 0, 0)')
ax.scatter(1, 0, 1, zdir='y', label='A(1, 0, 1)')

# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-40)

plt.show()

# verify
W = np.matrix([[1],
              [1],
              [0],
              [1]])

WP = np.matrix([[P[0, 0] - W[0, 0]],
                [P[1, 0] - W[1, 0]],
                [P[1, 0] - W[1, 0]],
              [0]])
WP1 = np.matrix([[P1[0, 0] - W[0, 0]],
                [P1[1, 0] - W[1, 0]],
                [P1[1, 0] - W[1, 0]],
              [0]])

AbsWP = math.sqrt(WP[0, 0] * WP[0, 0] + WP[1, 0] * WP[1, 0] + WP[2, 0] * WP[2, 0])
AbsWP1 = math.sqrt(WP1[0, 0] * WP1[0, 0] + WP1[1, 0] * WP1[1, 0] + WP1[2, 0] * WP1[2, 0])

DotProduct_WP_WP1 = WP[0, 0] * WP1[0, 0] + WP[1, 0] * WP1[1, 0] + WP[2, 0] * WP1[2, 0]
right = AbsWP1 * AbsWP * math.cos(math.pi / 6)

if DotProduct_WP_WP1 == right:
        print('Right')

