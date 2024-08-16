def othello(x):
    i_dx, j_dx, color = x[0] - 1, x[1] - 1, x[2]
    mat[i_dx][j_dx] = color
    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    pos = []
    for k in d:
        ik, jk = i_dx + k[0], j_dx + k[1]
        if 0 <= ik < N and 0 <= jk < N:
            if mat[ik][jk] != color and mat[ik][jk] != 0:
                pos.append(k)

    for k in pos:
        m = 1
        while True:
            ikm, jkm = i_dx + k[0] * m, j_dx + k[1] * m
            if not (0 <= ikm < N and 0 <= jkm < N):
                break
            if mat[ikm][jkm] == color:
                for i in range(1, m):
                    mat[i_dx + k[0] * i][j_dx + k[1] * i] = color
                break
            if mat[ikm][jkm] == 0:
                break
            m += 1




T = int(input())
for tc in range(T):
    N, M = map(int, input().split())        # N : 보드 크기 (4, 6, 8)
    game = [list(map(int, input().split())) for _ in range(M)]  # 1: 흑 2: 백 0: x

    mat = [[0] * N for _ in range(N)]
    c = N // 2
    mat[c][c] = mat[c-1][c-1] = 2
    mat[c-1][c] = mat[c][c-1] = 1
    print(game)
    for row in mat:
        print(row)
    print('***')

    for stone in game:
        othello(stone)
        print(stone)
        for row in mat:
            print(row)
        print('*')

    black = sum(row.count(1) for row in mat)
    white = sum(row.count(2) for row in mat)

    print(f'#{tc+1}', black, white)


    # while True:
    #     if i_idx + a < N - 1:
    #         if mat[i_idx + a][j_idx] != 0 and mat[i_idx + a][j_idx] != color:
    #             a += 1
    #             continue
    #         if mat[i_idx + a][j_idx] == color:
    #             for i in range(i_idx, i_idx + a):
    #                 mat[i][j_idx] = color
    #             break
    #     break
    #
    # a = 1
    # while True:
    #     if 0 < i_idx - a:
    #         if mat[i_idx - a][j_idx] != 0 and mat[i_idx - a][j_idx] != color:
    #             a += 1
    #             continue
    #         if mat[i_idx - a][j_idx] == color:
    #             for i in range(i_idx, i_idx - a - 1, -1):
    #                 mat[i][j_idx] = color
    #             break
    #     break
    #
    # a = 1
    # while True:
    #     if j_idx + a < N - 1:
    #         if mat[i_idx][j_idx + a] != 0 and mat[i_idx][j_idx + a] != color:
    #             a += 1
    #             continue
    #         if mat[i_idx][j_idx + a] == color:
    #             for j in range(j_idx, j_idx + a):
    #                 mat[i_idx][j] = color
    #             break
    #     break
    #
    # a = 1
    # while True:
    #     if 0 < j_idx - a:
    #         if mat[i_idx][j_idx - a] != 0 and mat[i_idx][j_idx - a] != color:
    #             a += 1
    #             continue
    #         if mat[i_idx][j_idx - a] == color:
    #             for j in range(j_idx, j_idx - a - 1, -1):
    #                 mat[i_idx][j] = color
    #             break
    #     break

