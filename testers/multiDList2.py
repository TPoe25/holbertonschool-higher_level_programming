import random
import math

listTable = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" || ")
    print()