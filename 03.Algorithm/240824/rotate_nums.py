def rotate(m):
    new_m = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_m[j][N - 1 - i] = m[i][j]
    return new_m


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(str, input().split())) for _ in range(N)]

    mat1 = rotate(mat)
    mat2 = rotate(mat1)
    mat3 = rotate(mat2)

    print(f'#{tc + 1}')
    for i in range(N):
        row = [''.join(mat1[i]), ''.join(mat2[i]), ''.join(mat3[i])]
        print(*row)
