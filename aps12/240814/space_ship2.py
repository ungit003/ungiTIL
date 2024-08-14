T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    mat = [[10] * (M + 2)] + [[10] + list(map(int, input().split())) + [10] for _ in range(N)] + [[10] * (M + 2)]

    # print(mat)
    ans_mat = 0
    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            count = 0
            for elem in d:
                a = mat[i][j]
                b = mat[i + elem[0]][j + elem[1]]
                if a > b:
                    count += 1
            if count >= 4:
                ans_mat += 1

    print(f'#{tc+1} {ans_mat}')
