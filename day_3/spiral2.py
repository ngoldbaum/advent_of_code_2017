import numpy as np

from spiral import navigate


NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, +1),
    (1, -1), (1, 0), (1, 1)
]

data = np.zeros((1001, 1001))

i0, j0 = 500, 500

maxval = 1

data[i0, j0] = 1

i, j = i0, j0

ind = 2

while maxval < 325489:
    x, y = navigate(ind)
    res = sum([data[i0 + x + n[0], j0 + y + n[1]] for n in NEIGHBORS])
    print(ind, res)
    data[i0 + x, j0 + y] = res
    if data[i0 + x, j0 + y] > maxval:
        maxval = data[i0 + x, j0 + y]
    ind += 1
    

print(maxval)
