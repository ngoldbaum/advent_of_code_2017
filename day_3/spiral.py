import numpy as np

number_per_shell = 4*(2*np.arange(100000) - 1) + 4
number_per_shell[0] = 1

cum_number_per_shell = np.cumsum(number_per_shell)


def navigate(input):
    if input == 1:
        return 0, 0
    shell_number = int(np.digitize(input, cum_number_per_shell, right=True))
    init_x = shell_number
    init_y = -shell_number + 1
    num_steps = input - cum_number_per_shell[shell_number-1] - 1
    if num_steps == 0 or shell_number == 0:
        return init_x, init_y
    cum_steps = 0
    x, y = init_x, init_y
    for i in range(2*(shell_number - 1) + 1):
        y += 1
        cum_steps += 1
        if cum_steps == num_steps:
            return x, y
    for i in range(2*shell_number):
        x -= 1
        cum_steps += 1
        if cum_steps == num_steps:
            return x, y
    for i in range(2*shell_number):
        y -= 1
        cum_steps += 1
        if cum_steps == num_steps:
            return x, y
    for i in range(2*shell_number):
        x += 1
        cum_steps += 1
        if cum_steps == num_steps:
            return x, y
    # should never get here
    import pdb; pdb.set_trace()
    raise RuntimeError


def get_number_of_steps(input):
    if input == 1:
        return 0
    x, y = navigate(input)
    return np.abs(x) + np.abs(y)


if __name__ == "__main__":
    print(get_number_of_steps(325489))
