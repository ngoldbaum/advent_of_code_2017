def advance_a(a):
    while True:
        a = (a * 16807) % 2147483647
        if a % 4 == 0:
            break
    return a


def advance_b(b):
    while True:
        b = (b * 48271) % 2147483647
        if b % 8 == 0:
            break
    return b


if __name__ == "__main__":
    a = 591
    b = 393
    count = 0
    for i in range(int(5e6)):
        if i % 1000000 == 0:
            print(i)
        a = advance_a(a)
        b = advance_b(b)
        sa = "{0:032b}".format(a)
        sb = "{0:032b}".format(b)
        if sa[-16:] == sb[-16:]:
            count += 1
    print(count)
