with open('input', 'r') as f:
    text = f.readlines()

text = [list(map(int, t.strip().split())) for t in text]

checksum = 0

for row in text:
    checksum += max(row) - min(row)

print(checksum)
