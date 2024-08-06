def straight(x, y):
    i = 0
    while True:
        i += 1
        if lad[x - i][y + 1] == 1:
            return right(x - i, y + 1)
        if lad[x - i][y - 1] == 1:
            return left(x - i, y - 1)
        if lad[x - i][y] == 0:
            return y


def right(x, y):
    j = 0
    while True:
        j += 1
        if lad[x][y + j] == 0:
            return straight(x, y + j - 1)


def left(x, y):
    k = 0
    while True:
        k += 1
        if lad[x][y - k] == 0:
            return straight(x, y - k + 1)


for _ in range(10):
    tc = int(input())
    lad = [[0] * 102] + [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    start = lad[100].index(2)
    result = straight(100, start)
    print(f'#{tc} {result - 1}')