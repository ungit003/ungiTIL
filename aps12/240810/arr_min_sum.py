# def dfs(x, visited, result):
#     wanna_sum = []
#     j_idx = 0
#     j_list = list(range(N))
#     for i in range(N):
#         j_elem = j_list[j_idx]
#         if j_elem not in visited:
#             j_elem = 0
#             visited.append(j_elem)
#         else:
#             j_idx += 1
#             j_elem = j_list[j_idx]
#             visited.append(j_elem)
#         wanna_sum.append(x[i][j_elem])
#     result.append(sum(wanna_sum))


def dfs(mat, current, adjm, visited, result):
    visited[current] = True
    
    for i in range(len(adjm)):
        if adjm[current][i] and not visited[i]:
            dfs(i, adjm, visited)


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    adjm = [[1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        adjm[i][i] = 0

    visited = [False] * N

    result = []

    for x in range(N):
        dfs(x, adjm, visited)

