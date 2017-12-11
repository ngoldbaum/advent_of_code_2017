from parser import clean

GARBAGE_EXAMPLES = {
    "<>": 0,
    "<random characters>": 17,
    "<<<<>": 3,
    "<{!>}>": 2,
    "<!!>": 0,
    "<!!!>>": 0,
    "<{o\"i!a,<{i<a>": 10,
}

for g, c in GARBAGE_EXAMPLES.items():
    assert clean(g) == ('', c)
