import numpy as np
from collections import defaultdict
from itertools import product

def add_tuples(t0, i, t1):
    return (t0[0] + i*t1[0], t0[1] + i*t1[1])


# Read and process the puzzle
f = open('input.txt')
ls = f.read().strip().split("\n")

board = defaultdict(str)
board |= {(i, j): x for i, l in enumerate(ls) for j, x in enumerate(l)}
octdir = {(i, j) for (i, j) in [(1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1)]}
diagdir1 = {(i, j) for (i, j) in [(1, 1), (-1, -1)]}
diagdir2 = {(i, j) for (i, j) in [(-1, 1), (1, -1)]}

print(sum(
    [board[add_tuples(loc, i,  dz)] for i in range(4)] == ["X", "M", "A", "S"]
    for loc in list(board.keys())
    for dz in octdir
    ))

count = 0
for loc in list(board.keys()):
    diagonal1 = False
    diagonal2 = False
    for dz in diagdir1:
        if [board[add_tuples(loc, i,  dz)] for i in range(-1, 2)] == ["M", "A", "S"]:
            diagonal1 = True
    for dz in diagdir2:
        if [board[add_tuples(loc, i,  dz)] for i in range(-1, 2)] == ["M", "A", "S"]:
            diagonal2 = True

    count += int(diagonal1 and diagonal2)
print(count)
    
