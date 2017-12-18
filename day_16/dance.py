import string

from collections import deque

NUM_DANCERS = 16


def dance(instructions, state):
    state = deque(state)

    for instruction in instructions:
        if instruction.startswith('s'):
            state.rotate(int(instruction[1:]))
        if instruction.startswith('x'):
            tm = list(map(int, instruction[1:].split('/')))
            state[tm[0]], state[tm[1]] = state[tm[1]], state[tm[0]]
        if instruction.startswith('p'):
            tm = instruction[1:].split('/')
            i0 = state.index(tm[0])
            i1 = state.index(tm[1])
            state[i0], state[i1] = state[i1], state[i0]

    return "".join(state)


if __name__ == "__main__":
    with open('input', 'r') as f:
        text = f.read()

    instructions = text.strip().split(',')

    init_state = string.ascii_lowercase[:NUM_DANCERS]
    state = init_state[:]
    i = 0

    while True:
        state = dance(instructions, state)
        i += 1
        if state == init_state:
            break

    for i in range(int(1e9) % 60):
        state = dance(instructions, state)

    print(state)
