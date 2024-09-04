def transpose(m):
    for i in range(N):
        for j in range(N):
            if i > j:
                m[i][j], m[j][i] = m[j][i], m[i][j]


def find(m):
    cnt = 0
    for row in m:
        for i in range(len(row)-1, -1, -1):
            if row[i] == '0':
                row.pop(i)
        finder = ''.join(row)
        for i in range(len(finder)-1):
            if finder[i] == '1' and finder[i+1] == '2':
                cnt += 1
    return cnt


T = 10
for tc in range(T):
    N = int(input())
    mat = [list(map(str, input().split())) for _ in range(N)]

    transpose(mat)
    ans = find(mat)
    print(f'#{tc+1}', ans)
