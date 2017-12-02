fn = open('input', 'r')

text = fn.readlines()[0]

d0 = text[0]

sum = 0

n = len(text)
offset = n//2

for i in range(n):
    if text[i] == text[(i + offset) % n]:
        sum += int(text[i])

print(sum)
