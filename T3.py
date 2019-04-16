# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt
import math

#
# Part I
#

fig = plt.figure()
ax = fig.gca(projection='3d')


def draw_line_with_2points(point1, point2, linelable):
    x = np.linspace(point1[0, 0], point2[0, 0], 10)
    kxy = (point1[1, 0] - point2[1, 0]) / (point1[0, 0] - point2[0, 0])
    bxy = (point2[0, 0] * point1[1, 0] - point1[0, 0] * point2[1, 0]) / (point2[0, 0] - point1[0, 0])
    y = kxy * x + bxy
    # y = k * x + b

    kxz = (point1[2, 0] - point2[2, 0]) / (point1[0, 0] - point2[0, 0])
    bxz = (point2[0, 0] * point1[2, 0] - point1[0, 0] * point2[2, 0]) / (point2[0, 0] - point1[0, 0])
    z = kxz * x + bxz
    # z = k * x + b

    ax.plot(x, y, z, zdir='z', label=linelable)
    return


def dot_product(vector1, vector2):
    return vector1[0, 0] * vector2[0, 0] + vector1[1, 0] * vector2[1, 0] + vector1[2, 0] * vector2[2, 0]


# cross product
# U（ux,uy,uz） V(vx,vy,vz)
# U x V = (uy·vz – uz·vy)i + (ux·vz-uz·vx)j + (ux·vy-uy·vx)z
def cross_product(vector2, vector1):
    return np.matrix([[vector1[1, 0] * vector2[2, 0] - vector1[2, 0] * vector2[1, 0]],
               [vector1[2, 0] * vector2[0, 0] - vector1[0, 0] * vector2[2, 0]],
               [vector1[0, 0] * vector2[1, 0] - vector1[1, 0] * vector2[0, 0]],
               [1]
               ])

# test cross product function
# test1 = np.matrix([[1],
#                 [2],
#                 [3],
#                 [0]
#                 ])
# test2 = np.matrix([[4],
#                 [5],
#                 [6],
#                 [0]
#                 ])
# print(cross_product(test1, test2))


# A(1, 1, 1); B(2, 2, 1); C(2, 1, 2)
A = np.matrix([[1],
                [1],
                [1],
                [0]
                ])
B = np.matrix([[2],
                [2],
                [1],
                [0]
                ])
C = np.matrix([[2],
                [1],
                [2],
                [0]
                ])
AB = np.matrix([[B[0, 0] - A[0, 0]],
                [B[1, 0] - A[1, 0]],
                [B[2, 0] - A[2, 0]],
                [1]
                ])
LenAB = math.sqrt(dot_product(AB, AB))

AC = np.matrix([[C[0, 0] - A[0, 0]],
                [C[1, 0] - A[1, 0]],
                [C[2, 0] - A[2, 0]],
                [1]
                ])
LenAC = math.sqrt(dot_product(AC, AC))

ax.scatter(A[0, 0], A[1, 0], A[2, 0], zdir='a', label='A(1, 1, 1)')
ax.scatter(B[0, 0], B[1, 0], B[2, 0], zdir='b', label='B(2, 2, 1)')
ax.scatter(C[0, 0], C[1, 0], C[2, 0], zdir='c', label='C(2, 1, 2)')


u = np.matrix([[AB[0, 0] / LenAB],
               [AB[1, 0] / LenAB],
               [AB[2, 0] / LenAB],
               [1]
               ])
print('len u:')
print(math.sqrt(dot_product(u, u)))
# ok

crossProduct_AC_AB = cross_product(AC, AB)
dotProduct_AB_AC = dot_product(AB, AC)
cos_AB_AC = dotProduct_AB_AC / (LenAB * LenAC)

LenCrossProduct_AC_AB = LenAC * LenAB * math.sqrt(1 - cos_AB_AC * cos_AB_AC)

v = np.matrix([[crossProduct_AC_AB[0, 0] / LenCrossProduct_AC_AB],
               [crossProduct_AC_AB[1, 0] / LenCrossProduct_AC_AB],
               [crossProduct_AC_AB[2, 0] / LenCrossProduct_AC_AB],
               [1]
               ])
print('len v:')
print(math.sqrt(dot_product(v, v)))

n = cross_product(u, v)
print('len n:')
print(math.sqrt(dot_product(n, n)))

draw_line_with_2points(A, A + u, 'u')
draw_line_with_2points(A, A + v, 'v')
draw_line_with_2points(A, A + n, 'n')

print('dot product u & v :')
print(dot_product(u, v))
print('dot product u & n :')
print(dot_product(u, n))
print('dot product n & v :')
print(dot_product(n, v))


ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=12., azim=18)

#
# Part II
#
uvn2xyzMatrix = np.matrix([[u[0, 0], u[1, 0], u[2, 0], 0],
                           [v[0, 0], v[1, 0], v[2, 0], 0],
                           [n[0, 0], n[1, 0], n[2, 0], 0],
                           [0, 0, 0, 1]])
translateBackMatrix = np.matrix([[1, 0, 0, 1],
                           [0, 1, 0, 1],
                           [0, 0, 1, 1],
                           [0, 0, 0, 1]])
uvn2xyzMatrix = translateBackMatrix * uvn2xyzMatrix


print('uvn2xyzMatrix:')
print(uvn2xyzMatrix)

#
# Part III
#
Puvn = np.matrix([[1],
               [1],
               [1],
               [1]])
Pxyz = uvn2xyzMatrix * Puvn

ax.scatter(Pxyz[0, 0], Pxyz[1, 0], Pxyz[2, 0], zdir='d', label='Pxyz')

print('Pxyz:')
print(Pxyz)
ax.legend()
plt.show()
