import numpy as np

locids = np.genfromtxt('input.txt', delimiter='   ', dtype=float)
locids[:, 0] = np.sort(locids[:, 0])
locids[:, 1] = -1 * np.sort(locids[:, 1])

diff = np.abs(np.sum(locids, axis=1))
print(np.sum(diff))


## PART 2

N = locids.shape[0]
idx = np.zeros((N, N))

for i in range(N):
    idx[i, :] = locids[i, 0] == -locids[:, 1]
similarity = np.sum(idx, axis=1)
print(np.sum(locids[:, 0] * similarity))
