T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    sum_list = []
    for i in range(N):
        for j in range(M):
            K = mat[i][j]
            sum_flo = K
            for ii in range(1, K+1):
                if 0 <= i + ii < N:
                    flo_s = mat[i + ii][j]
                    sum_flo += flo_s
                if 0 <= i - ii < N:
                    flo_s = mat[i - ii][j]
                    sum_flo += flo_s

            for jj in range(1, K+1):
                if 0 <= j + jj < M:
                    flo_s = mat[i][j + jj]
                    sum_flo += flo_s
                if 0 <= j - jj < M:
                    flo_s = mat[i][j - jj]
                    sum_flo += flo_s

            sum_list.append(sum_flo)
    print(f'#{tc+1} {max(sum_list)}')
