with open('input', 'r') as f:
    text = f.readlines()

text = [t.strip() for t in text]

count = 0

for t in text:
    words = t.split()
    if len(set(words)) == len(words):
        count += 1

print(count)
