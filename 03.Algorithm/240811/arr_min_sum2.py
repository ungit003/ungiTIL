def dfs(mat, start, visited, wanna_sum, result, floor):
    vst = [visited[j] for j in range(N)]
    vst[start] = 1
    wanna_sum.append(mat[floor][start])
    print(wanna_sum)

    if floor < N-1:
        floor += 1
        for i in range(N):
            if vst[i] != 1:
                dfs(mat, i, vst, wanna_sum, result, floor)
    else:
        result.append(sum(wanna_sum))
        wanna_sum.clear()


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    sp = list(range(N))
    visited = [0] * N
    wanna_sum = []
    result = []
    floor = 0
    for elem in sp:
        dfs(arr, elem, visited, wanna_sum, result, floor)
        print(result)
