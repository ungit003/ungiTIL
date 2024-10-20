def dfs(adjL, start, start2, visited, wanna, result, floor):
    visited2 = [visited[i] for i in range(len(visited))]
    visited2.append(start)
    wanna += mat[floor][start]
    floor += 1

    if floor < N:
        for neighbor in adjL[start]:
            if neighbor not in visited:
                dfs(adjL, neighbor, start2, visited, wanna, result, floor)
    else:
        result.append(wanna)


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    adjL = {}
    for i in range(N):
        a = list(range(N))
        a.remove(i)
        adjL[i] = a
    # print(adjL)

    visited = []
    result = []
    start_point = list(range(N))
    wanna = 0
    floor = 0
    for i in range(N):
        dfs(adjL, i, i, visited, wanna, result, floor)
    print(result)
    print(f'#{tc+1}', min(result))
