fn = open('input', 'r')

text = fn.readlines()[0]

d0 = text[0]

sum = 0

for d1 in (text[1:] + d0):
    if d0 == d1:
        sum += int(d0)
    d0 = d1

print(sum)
