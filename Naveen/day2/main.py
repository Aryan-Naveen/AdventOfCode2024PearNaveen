import numpy as np


def saferow1(row):
    diff =  np.diff(row)
    return np.logical_and(diff <= -1, diff >= -3).all() or  np.logical_and(diff >= 1, diff <= 3).all()

f = open("input.txt")
data = f.read().splitlines()

safecount = 0
for row in data:
    row = np.array([float(val) for val in row.split(' ')])
    safecount += int(saferow1(row))

print(safecount)



def saferow2(row):
    safe = False
    if saferow1(row):
        safe = True
    for i in range(len(row)):
        row_ = row.copy()
        row_ = np.delete(row_, i)
        if saferow1(row_):
            safe = True
            break
    return safe
    
safecount = 0
for row in data:
    row = np.array([float(val) for val in row.split(' ')])
    safecount += int(saferow2(row))

print(safecount)
