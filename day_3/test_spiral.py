from spiral import get_number_of_steps

answers = {
    1: 0,
    12: 3,
    23: 2,
    1024: 31
}

for input, output in answers.items():
    assert get_number_of_steps(input) == output
