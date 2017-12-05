with open('input', 'r') as f:
    text = f.readlines()

instructions = [int(t.strip()) for t in text]

print(instructions)

pos = 0
count = 0

while 0 <= pos < len(instructions):
    count += 1
    old_pos = pos
    pos += instructions[pos]
    if instructions[old_pos] >= 3:
        instructions[old_pos] -= 1
    else:
        instructions[old_pos] += 1

print(count)
