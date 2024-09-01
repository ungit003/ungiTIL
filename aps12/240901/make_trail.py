"""def find_top(arr):
    size = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] > size:
                size = mat[i][j]
                arr.clear()
                arr.append((i, j))
            elif mat[i][j] == size:
                arr.append((i, j))


def find_trail(spot, lth):
    # i, j = spot
    # for k in range(4):
    #     di, dj = i + dr[k][0], j + dr[k][1]
    #     if 0 <= di < N and 0 <= dj < N:
    #         if mat[i][j] > mat[di][dj]:
    #             lth += 1
    #             find_trail((di, dj), lth)
    # ans = lth
    # lth = 1
    # return ans
    i, j = spot
    now = mat[i][j]
    while True:
        can_go = []
        for k in range(4):
            di, dj = i + dr[k][0], j + dr[k][1]
            if 0 <= di < N and 0 <= dj < N:
                if mat[i][j] > mat[di][dj]:
                    can_go.append((di, dj))




T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    t_list = []
    find_top(t_list)
    print(t_list)

    max_trail = 0
    length = 1
    dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for top in t_list:
        trail = find_trail(top, length)
        max_trail = max(max_trail, trail)

    print(f'#{tc+1}', max_trail)"""

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def dfs(r, c, chance):
    global MAX, visited
    MAX = max(MAX, visited[r][c])
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue
        if A[r][c] > A[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance)
            visited[nr][nc] = 0
        elif chance and A[nr][nc] - K < A[r][c]:
            temp = A[nr][nc]
            A[nr][nc] = A[r][c] - 1
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance - 1)
            visited[nr][nc] = 0
            A[nr][nc] = temp


# main
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = []
    top = 0
    for i in range(N):
        A.append(list(map(int, input().split())))
        for j in range(N):
            if A[i][j] > top:
                top = A[i][j]
    MAX = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0

    print("#{} {}".format(tc + 1, MAX))
