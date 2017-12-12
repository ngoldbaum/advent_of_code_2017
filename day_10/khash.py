import numpy as np
import operator
from functools import reduce

from knots import advance

SALT = [17, 31, 73, 47, 23]


def dense_hash(sparse_hash):
    ret = []
    for i in range(16):
        subset = sparse_hash[i*16:(i+1)*16]
        result = reduce(operator.xor, subset)
        hex = format(result, 'x')
        hex = str.zfill(hex, 2)
        ret.append(hex)
    return "".join(ret)


def khash(input_string):
    input_stream = []
    for c in input_string:
        input_stream.append(ord(c))

    input_stream += SALT

    state = np.arange(256)
    position = 0
    skip_size = 0

    for _ in range(64):
        for length in input_stream:
            state, position, skip_size = advance(
                state, position, length, skip_size)

    return dense_hash(state)


if __name__ == "__main__":
    input_string = "189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62"
    print(khash(input_string))
