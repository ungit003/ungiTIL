T = int(input())
for tc in range(T):
    A, B, C = map(int, input().split())

    A, B, C = A-1, B-1, C-1

    poss = True
    eat = 0

    b = B
    while True:
        if b < C:
            break
        if b == 0:
            poss = False
            break
        b -= 1
        eat += 1

    a = A
    while True:
        if a < b:
            break
        if a == 0:
            poss = False
            break
        a -= 1
        eat += 1

    if not poss:
        eat = -1
    print(f'#{tc+1}', eat)
