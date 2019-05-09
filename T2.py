import numpy as np
import matplotlib.pyplot as plt
import math

xAB = np.linspace(2, 7, 100)
yAB = (3 * xAB - 1) / 5
plt.plot(xAB, yAB, label='AB')
# draw vector AB

P1 = np.matrix([[4],
              [1],
              [0],
              [1]])

P2 = np.matrix([[6],
              [1],
              [0],
              [1]])

TranslationToOMatrix = np.matrix([[1, 0, 0, -2],
                         [0, 1, 0, -1],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]
                         )
# Translate to O point

RotateNegZMatrix = np.matrix([[math.cos(-1 * math.atan(3 / 5)), -1 * math.sin(-1 * math.atan(3 / 5)), 0, 0],
                         [math.sin(-1 * math.atan(3 / 5)), math.cos(-1 * math.atan(3 / 5)), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]
                         )

# Rotate to X axis

ScaleYMatrix = np.matrix([[1, 0, 0, 0],
                         [0, -1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]
                         )
# Mirror

RotatePosZMatrix = np.matrix([[math.cos(math.atan(3 / 5)), -1 * math.sin(math.atan(3 / 5)), 0, 0],
                         [math.sin(math.atan(3 / 5)), math.cos(math.atan(3 / 5)), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]
                         )
# Rotate from X axis

TranslationFromOMatrix = np.matrix([[1, 0, 0, 2],
                         [0, 1, 0, 1],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]
                         )
# Translate from O point

P11 = TranslationFromOMatrix * RotatePosZMatrix * ScaleYMatrix * RotateNegZMatrix * TranslationToOMatrix * P1
P22 = TranslationFromOMatrix * RotatePosZMatrix * ScaleYMatrix * RotateNegZMatrix * TranslationToOMatrix * P2
# Change

xP1P2 = np.linspace(P1[0, 0], P2[0, 0], 100)
yP1P2 = xP1P2 / xP1P2
plt.plot(xP1P2, yP1P2, label='P1P2')
# draw vector P1P2

xP11P22 = np.linspace(P11[0, 0], P22[0, 0], 100)
kP11P22 = (P11[1, 0] - P22[1, 0]) / (P11[0, 0] - P22[0, 0])
bP11P22 = (P22[0, 0] * P11[1, 0] - P11[0, 0] * P22[1, 0]) / (P22[0, 0] - P11[0, 0])
yP11P22 = kP11P22 * xP11P22 + bP11P22
# y = k * x + b

plt.plot(xP11P22, yP11P22, label='P11P22')
# draw vector P11P22

plt.scatter(2, 1, label='A')
plt.scatter(7, 4, label='B')
plt.scatter(P1[0, 0], P1[1, 0], label='P1')
plt.scatter(P2[0, 0], P2[1, 0], label='P2')
plt.scatter(P11[0, 0], P11[1, 0], label='P11')
plt.scatter(P22[0, 0], P22[1, 0], label='P22')

plt.xticks(range(0, 9, 1))
plt.yticks(range(0, 8, 1))
plt.legend()
plt.show()

# verify
DotProduct_AB_P2P22 = (7 - 2) * (P2[0, 0] - P22[0, 0]) + (4 - 1) * (P2[1, 0] - P22[1, 0])
center_X_P2P22 = (P2[0, 0] + P22[0, 0]) / 2
center_Y_P2P22 = (P2[1, 0] + P22[1, 0]) / 2
difP2P22 = math.fabs(center_Y_P2P22 - (3 * center_X_P2P22 - 1) / 5)
if math.fabs(DotProduct_AB_P2P22) < 0.00000000001 and difP2P22 < 0.00000000001:
    print('Right2')

DotProduct_AB_P1P11 = (7 - 2) * (P1[0, 0] - P11[0, 0]) + (4 - 1) * (P1[1, 0] - P11[1, 0])
center_X_P1P11 = (P1[0, 0] + P11[0, 0]) / 2
center_Y_P1P11 = (P1[1, 0] + P11[1, 0]) / 2
difP1P11 = math.fabs(center_Y_P1P11 - (3 * center_X_P1P11 - 1) / 5)
if math.fabs(DotProduct_AB_P1P11) < 0.00000000001 and difP1P11 < 0.00000000001:
    print('Right1')
