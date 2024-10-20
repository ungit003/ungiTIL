def sp(m):
    arr = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == 0:
                arr.append((i, j))
    return arr


def game(stt, drt):
    cnt = 0
    i, j = stt

    def direction_change(num, drt):
        if num == 5:
            new_drt = (drt + 2) % 4

        else:
            if num % 4 == drt:
                new_drt = (drt - 1) % 4

            elif (num + 1) % 4 == drt:
                new_drt = (drt + 1) % 4

            else:
                new_drt = (drt + 2) % 4
        return new_drt

    def jump(x, y):
        stt_warm = mat[x][y]
        for nx in range(N):
            for ny in range(N):
                if mat[nx][ny] == stt_warm and (nx, ny) != (x, y):
                    return nx, ny
        return None, None

    while True:
        i, j = i + d[drt][0], j + d[drt][1]

        if not (0 <= i < N) or not (0 <= j < N):
            drt = direction_change(5, drt)
            cnt += 1
            continue

        elif mat[i][j] in [1, 2, 3, 4, 5]:
            drt = direction_change(mat[i][j], drt)
            cnt += 1
        elif mat[i][j] in [6, 7, 8, 9, 10]:
            i, j = jump(i, j)

        if (i, j) == stt:
            break

        if mat[i][j] == -1:
            break
    return cnt


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    stt_list = sp(mat)
    max_score = 0
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for elem in stt_list:
        for k in range(4):
            max_score = max(game(elem, k), max_score)

    print(f'#{tc + 1}', max_score)
