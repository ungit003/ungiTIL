T = int(input())
for tc in range(T):
    N = int(input())
    mat = [[s for s in input()] for _ in range(N)]

    result = 'NO'

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'o':
                # 가로
                if j < N - 4:
                    finder = set()
                    for k in range(5):
                        finder.add(mat[i][j + k])
                    if len(finder) == 1:
                        result = 'YES'
                # 세로
                if i < N - 4:
                    finder = set()
                    for k in range(5):
                        finder.add(mat[i + k][j])
                    if len(finder) == 1:
                        result = 'YES'
                # 대각선 \
                if j < N - 4 and i < N - 4:
                    finder = set()
                    for k in range(5):
                        finder.add(mat[i + k][j + k])
                    if len(finder) == 1:
                        result = 'YES'
                # 대각선 /
                if 3 < j and i < N - 4:
                    finder = set()
                    for k in range(5):
                        finder.add(mat[i + k][j - k])
                    if len(finder) == 1:
                        result = 'YES'

    print(f'#{tc + 1}', result)
