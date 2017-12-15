import numpy as np
from bitstring import BitArray
from skimage.measure import label

from khash import khash


if __name__ == "__main__":
    num_on = 0
    arr = np.zeros((128, 128))
    for i in range(128):
        seed = 'xlqgujun' + '-' + str(i)
        hash = khash(seed)
        bin = BitArray(hex=hash).bin
        arr[i] = np.array([int(b) for b in bin])
    print(np.sum(arr == 0))
    _, num_regions = label(arr, connectivity=1, return_num=True)
    print(num_regions)
