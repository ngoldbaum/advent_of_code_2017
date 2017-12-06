with open('input', 'r') as f:
    text = f.read()

blocks_per_bank = [int(t) for t in text.split()]

old_configurations = []
num_sweeps = 0
num_blocks = len(blocks_per_bank)

while blocks_per_bank not in old_configurations:
    old_configurations.append(blocks_per_bank[:])
    blocks_to_redistribute = max(blocks_per_bank)
    index = blocks_per_bank.index(blocks_to_redistribute)
    blocks_per_bank[index] = 0
    while blocks_to_redistribute > 0:
        index += 1
        if index >= num_blocks:
            index = 0
        blocks_per_bank[index] += 1
        blocks_to_redistribute -= 1
    num_sweeps += 1
    print(blocks_per_bank)

print(num_sweeps)
