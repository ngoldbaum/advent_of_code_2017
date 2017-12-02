import itertools

with open('input', 'r') as f:
    text = f.readlines()

text = [list(map(int, t.strip().split())) for t in text]

checksum = 0

for row in text:
    for pair in itertools.combinations(row, 2):
        if pair[1] % pair[0] == 0:
            checksum += pair[1] // pair[0]
        elif pair[0] % pair[1] == 0:
            checksum += pair[0] // pair[1]

print(checksum)
