
import numpy as np
data = f = open("Input2.txt")
data = f.read().splitlines()
    

#for every row, check the numbers in each column of row to see that they are all decreasing or increasing
#then if true, check for everything to be increasing or decreasing by 3 or less


def saferow (row):
    safe = True
    diff = np.diff(row)
    for i in diff:
        if abs(i) > 3 or abs(i) <= 0:
            safe = False
    for index in range(len(diff) - 1):
        current = diff[index] 
        nex = diff[index + 1]
        if (nex > 0 and current < 0) or (current > 0 and nex < 0):
            safe = False
    return safe

def saferow2 (row):
    #if row already safe return true
    #if row not safe / for loop for every index remove index from row / run saferow function / if safe return true
    if saferow(row) == True:
        return True
    for index in range(len(row)):
        rowcopy = row.copy()
        rowcopy = np.delete(rowcopy, index)
        if saferow(rowcopy) == True:
            return True
    return False

count = 0

for row in data:
    row = np.array([float(val) for val in row.split(' ')])
    safe = saferow2(row)
    if safe == True:
        count += 1
print (count)






