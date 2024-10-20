def dfs(graph, start, end, visited, result):
    visited.add(start)
    result.append(start)

    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(graph, neighbor, end, visited, result)


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    path_list = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    # print(V, E, S, G, path_list)

    path_graph = {}
    for elem in path_list:
        if elem[0] not in path_graph:
            path_graph[elem[0]] = [elem[1]]
        else:
            path_graph[elem[0]].append(elem[1])

    # print(path_graph)

    start_point = S
    end_point = G
    mark = set()
    route = []

    dfs(path_graph, start_point, end_point, mark, route)

    if end_point in mark:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')
