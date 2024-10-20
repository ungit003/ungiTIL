T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            com_v = 0
            for k in range(5):
                d = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
                di = i + d[k][0]
                dj = j + d[k][1]
                if 0 <= di < N and 0 <= dj < M:
                    com_v += mat[di][dj]
            if max_v < com_v:
                max_v = com_v

    print(f'#{tc+1} {max_v}')
