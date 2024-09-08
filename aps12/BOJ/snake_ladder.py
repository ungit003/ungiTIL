def dfs(s, c):
    global min_v
    # print(s, c)
    if c >= min_v:
        return
    if s == 100:
        min_v = min(min_v, c)
        return

    for elem in lds:
        if s == elem[0]:
            s = elem[1]

    for elem in snk:
        if s == elem[0]:
            if not visited:
                visited[s] = 1
                s = elem[1]
                visited[s] = 0

    for i in dice:
        if s+i in poss or s+i in impo:
            dfs(s+i, c+1)
    if s < 94:
        dfs(s+6, c+1)
    if 94 <= s < 100:
        dfs(100, c+1)


def no_snk(s, c):
    global min_v
    # print(s, c)
    if c >= min_v:
        return
    if s == 100:
        min_v = min(min_v, c)
        return

    for elem in lds:
        if s == elem[0]:
            s = elem[1]

    for i in dice:
        if s+i > 100:
            continue
        if s+i not in poss and s+i not in impo:
            dfs(s+i, c+1)
        elif s+i in impo:
            continue
        elif s+i in poss:
            dfs(s+i, c+1)


N, M = map(int, input().split())
lds = [list(map(int, input().split())) for _ in range(N)]
poss = [elem[0] for elem in lds]
snk = [list(map(int, input().split())) for _ in range(M)]
impo = [elem[0] for elem in snk]
visited = [0] * 100

# print(lds, snk)
dice = list(range(1, 7))
min_v = float('inf')
no_snk(1, 0)
dfs(1, 0)
print(min_v)
