"""
풀이 전략
상하좌우로 움직일 수 있음. +1 일 경우만. 델타.
1차이가 없으면 스킵. 되나?
필요한 값. 스타트 지점 밸류, 좌표
"""


def find(m):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                di, dj, stt = i + d[k][0], j + d[k][1], m[i][j]
                if not (0 <= di < N and 0 <= dj < N):
                    continue
                if m[di][dj] == stt + 1:
                    route(stt, i, j, i, j)


def route(s, x, y, xi, yi):
    for k in range(4):
        dx, dy = x + d[k][0], y + d[k][1]
        if not (0 <= dx < N and 0 <= dy < N):
            continue
        if mat[dx][dy] == mat[x][y] + 1:
            cnt[xi][yi] += 1
            route(s, dx, dy, xi, yi)
    return


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cnt = [[1] * N for _ in range(N)]
    find(mat)

    max_v = 0
    min_s = []
    for i in range(N):
        for j in range(N):
            if cnt[i][j] > max_v:
                max_v = cnt[i][j]
                min_s.clear()
                min_s.append(mat[i][j])

            if cnt[i][j] == max_v:
                min_s.append(mat[i][j])

    print(f'#{tc+1}', min(min_s), max_v)
