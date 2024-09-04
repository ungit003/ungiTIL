def finder1(m):
    global flag
    d = [(0, 1), (1, 1), (1, 0), (1, -1)]
    for i in range(N):
        for j in range(N):
            if m[i][j] == 'o':
                print('1', i, j)
                for k in range(4):
                    x = 1
                    while True:
                        if x == 5:
                            flag = True
                            return
                        di, dj = i + d[k][0] * x, j + d[k][1] * x
                        if not(0 <= di < N and 0 <= dj < N):
                            print('2', k, di, dj)
                            break
                        if m[di][dj] != 'o':
                            print('3',k, di, dj)
                            break
                        x += 1


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [[s for s in input()] for _ in range(N)]

    flag = False
    finder1(mat)
    print(flag)
    if flag:
        print(f'#{tc+1}', 'YES')
    else:
        print(f'#{tc+1}', 'NO')

def finder1(m):
    d = [(0, 1), (1, 1), (1, 0), (1, -1)]
    N = len(m)

    for i in range(N):
        for j in range(N):
            if m[i][j] == 'o':
                for k in range(4):
                    x = 1
                    while True:
                        if x == 5:
                            return True
                        di, dj = i + d[k][0] * x, j + d[k][1] * x
                        if not (0 <= di < N and 0 <= dj < N):
                            break
                        if m[di][dj] != 'o':
                            break
                        x += 1
    return False


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [[s for s in input()] for _ in range(N)]

    if finder1(mat):
        print(f'#{tc + 1} YES')
    else:
        print(f'#{tc + 1} NO')