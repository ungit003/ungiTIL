T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))
    mat = []
    for i in range(N):
        raw = list(map(int, input().split()))
        mat.append(raw)

    # max_kill = 0
    # kill_mat = [[0] * (N - M + 1) for _ in range(N - M + 1)]
    # for i in range(N - M + 1):
    #     for j in range(N - M + 1):
    #     kill_mat[i][j] = mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]

    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            killing = 0
            for ii in range(M):
                for jj in range(M):
                    kill = mat[i+ii][j+jj]
                    killing += kill
            if killing > max_kill:
                max_kill = killing

    print(f'#{tc+1}', max_kill)

