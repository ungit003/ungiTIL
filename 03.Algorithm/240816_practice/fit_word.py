def counting(mat):
    cnt = 0
    for i in range(N + 1):
        for j in range(N - K + 1):
            if mat[i][j:j + K + 2] == [0] + [1] * K + [0]:
                cnt += 1

    transpose(mat)
    for i in range(N + 1):
        for j in range(N - K + 1):
            if mat[i][j:j + K + 2] == [0] + [1] * K + [0]:
                cnt += 1
    return cnt


def transpose(mat):
    for i in range(N + 2):
        for j in range(N + 2):
            if i < j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    mat = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]

    print(f'#{tc+1}', counting(mat))
