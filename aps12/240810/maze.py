def dfs(mat, start, end, visited, result):
    if end in visited:
        return

    d_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result.append(tuple(start))
    visited.add(tuple(start))

    check_list = []
    for elem in d_list:
        check_point = (start[0] + elem[0], start[1] + elem[1])
        if 0 <= check_point[0] < N and 0 <= check_point[1] < N:
            if mat[check_point[0]][check_point[1]] == 0 or mat[check_point[0]][check_point[1]] == 3:
                check_list.append(check_point)

    for cp in check_list:
        if cp not in visited:
            dfs(mat, cp, end, visited, result)


T = int(input())
for tc in range(T):
    N = int(input())
    maze = [[int(s) for s in input()] for _ in range(N)]

    # for row in maze:
        # print(row)

    visited = set()
    result = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sp = (i, j)
            if maze[i][j] == 3:
                ep = (i, j)

    # print(sp, ep)

    dfs(maze, sp, ep, visited, result)
    # print(visited)
    # print(result)

    if ep in visited:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')
