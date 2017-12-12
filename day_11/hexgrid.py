import operator

DIRECTION_OFFSETS = {
    'ne': (1, 1),
    'n': (0, 1),
    'nw': (-1, 0),
    'sw': (-1, -1),
    's': (0, -1),
    'se': (1, 0),
}


def norm(x, y):
    if (x*y < 0):
        return abs(x) + abs(y)
    return max(abs(x), abs(y))


def num_steps(path):
    steps = path.split(',')
    position = (0, 0)
    maxdist = 0
    for step in steps:
        position = tuple(map(operator.add, position, DIRECTION_OFFSETS[step]))
        n = norm(*position)
        maxdist = max(n, maxdist)
    return norm(*position), maxdist


if __name__ == "__main__":
    with open('input', 'r') as f:
        text = f.read().strip()

    print(num_steps(text))
