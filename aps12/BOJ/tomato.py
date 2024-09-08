from collections import deque


def bfs():
    day = 0
    arr = deque()
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                arr.append([day, (i, j)])
    # print(arr)

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while arr:
        x = arr.popleft()
        # print(x, arr)
        if day != x[0]:
            day += 1
        for k in range(4):
            di, dj = x[1][0] + d[k][0], x[1][1] + d[k][1]
            if not (0 <= di < N and (0 <= dj < M)):
                continue
            if mat[di][dj] == 0:
                arr.append([day+1, (di, dj)])
                mat[di][dj] = 1

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0:
                day = -1
    return day


M, N = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

ans = bfs()
print(ans)
