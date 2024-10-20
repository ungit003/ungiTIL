def making(i, j, c, b):
    for k in range(4):
        di, dj = i + d[k][0], j + d[k][1]
        if 0 <= di < N and 0 <= dj < N:
            if b:
                for x in range(1, K + 1):
                    mat[di][dj] -= x
                    if mat[di][dj] < mat[i][j]:
                        b = False
                        c += 1
                        making(di, dj, c, b)

            else:
                if mat[di][dj] < mat[i][j]:
                    c += 1
                    making(di, dj, c, b)

                else:
                    return c


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    mount_dict = {}
    for i in range(N):
        for j in range(N):
            if mat[i][j] not in mount_dict:
                mount_dict[mat[i][j]] = [(i, j)]
            else:
                mount_dict[mat[i][j]].append((i, j))
    print(mount_dict)

    max_mount = max(mount_dict)
    print(max_mount)

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cnt = 1
    brk = True

    c_max = 0
    for elem in mount_dict[max_mount]:
        x = making(elem[0], elem[1], cnt, brk)
        if c_max < x:
            c_max = x
    print(c_max)
