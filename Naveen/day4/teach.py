import numpy as np
with open ("simple.txt" , "r") as file:
    lines = file.readlines()
grid = []


for line in lines:
    row = line.strip().split()
    grid.append(list(row[0]))

grid = np.array(grid)

print(grid[0, 0])