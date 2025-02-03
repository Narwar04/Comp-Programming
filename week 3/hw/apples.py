import numpy as np

row, col = map(int, input().split())

tree_array = np.zeros((row, col))

for i in range(row):
    for j in range(col):
        tree_array[i][j] = str(input().strip().strip())
print (tree_array)