def search_row(m):
    global res
    for row in m:
        if len(set(row)) != N:
            res = False


def tp(m):
    for i in range(N):
        for j in range(N):
            if i > j:
                m[i][j], m[j][i] = m[j][i], m[i][j]


def search_sub(m):
    global res
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = set()
            for x in range(3):
                for y in range(3):
                    check.add(m[i+x][j+y])
            if len(check) != N:
                res = False
                return


T = int(input())
for tc in range(T):
    N = 9
    mat = [list(map(int, input().split())) for _ in range(N)]

    res = True
    search_row(mat)
    tp(mat)
    search_row(mat)
    search_sub(mat)
    if res:
        ans = 1
    else:
        ans = 0
    print(f'#{tc+1}', ans)
