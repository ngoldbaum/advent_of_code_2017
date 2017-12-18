size = 1
position = 0
save = None

for i in range(1, int(5e7)+1):
    if i % 1000 == 0:
        print(i)
    position = (position + 335) % size + 1
    size += 1
    if position == 1:
        save = i

print(save)
