def relay(x, y, lev):
    global res
    if lev == 6:
        ans.add(int(''.join(res)))
        return
    for k in range(4):
        dx, dy = x + d[k][0], y + d[k][1]
        if not (0 <= dx < 4 and 0 <= dy < 4):
            continue
        lev += 1
        res.append(mat[dx][dy])
        relay(dx, dy, lev)
        lev -= 1
        res.pop()


T = int(input())
for tc in range(T):
    mat = [list(map(str, input().split())) for _ in range(4)]

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = set()
    for i in range(4):
        for j in range(4):
            res = [mat[i][j]]
            relay(i, j, 0)

    print(f'#{tc+1}', len(ans))
