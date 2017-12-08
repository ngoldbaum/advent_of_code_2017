import operator

DISPATCH_TABLE = {
    'inc': operator.add,
    'dec': operator.sub,
    '>': operator.gt,
    '>=': operator.ge,
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
}


if __name__ == "__main__":
    with open('input', 'r') as f:
        text = f.readlines()

    instructions = [t.strip().split() for t in text]

    registers = set([i[0] for i in instructions])

    state = {}
    for r in registers:
        state[r] = 0

    maxval = 0

    for i in instructions:
        if DISPATCH_TABLE[i[5]](state[i[4]], int(i[6])):
            state[i[0]] = DISPATCH_TABLE[i[1]](state[i[0]], int(i[2]))
        maxval = max(maxval, max(state.values()))

    print(max(state.values()))
    print(maxval)
