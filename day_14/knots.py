import numpy as np


def advance(inp, position, length, skip_size):
    indices = []
    for i in range(position, position+length):
        indices.append(i % len(inp))
    position = (position + length + skip_size) % len(inp)
    skip_size += 1
    ret = inp.copy()
    ret[indices] = np.flip(ret[indices], 0)
    return ret, position, skip_size


if __name__ == "__main__":
    state = np.arange(256)
    position = 0
    skip_size = 0
    for length in [189, 1, 111, 246, 254, 2, 0, 120, 215, 93, 255, 50, 84,
                   15, 94, 62]:
        state, position, skip_size = advance(
            state, position, length, skip_size)
    print(state[0]*state[1])
