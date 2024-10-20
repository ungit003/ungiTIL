'''
1. 아무 엣지도 연결되지 않은 노드를 visit, res 저장
2. 들어오는 엣지가 없는 노드를 visit, res 저장
2-1. 2의 노드와 연결된 노드 중, 들어오는 노드가 다 visited이면 que에 저장
    -> 연결되어있는 모든 노드를 확인 해야되니까 매트릭스가 더 나은듯?
3. que에 쌓인 순서대로 노드를 visit, res 저장
4. res 출력
'''
import sys
sys.stdin = open("work_process_input.txt", "r")
from collections import deque


def process(e, m):
    check_li = set()
    can_come = set()
    que = deque()

    # 연결되어 있는 것, 받는 엣지가 있는 것 체크
    for elem in e:
        check_li.add(elem[0])
        check_li.add(elem[1])
        can_come.add(elem[1])

    # 1.
    for i in range(1, V + 1):
        if i not in check_li:
            visited[i] = 1
            res.append(i)
    # print(visited)
    # print(res)
    # print('-')

    # 2.
    no_come = list(set(range(1, V+1)) - can_come)
    for elem in no_come:
        visited[elem] = 1
        res.append(elem)
        que.append(elem)
    # print(visited)
    # print(res)
    # print(que)
    # print('-')

    # 2-1.
    while que:
        # que에서 맨 앞 값 pop : 8
        a = que.popleft()
        # print(a)

        # a와 연결되어 있는 노드
        connected = []
        for j in range(1, V + 1):
            if m[a][j] == 1:
                connected.append(j)

        # 노드에 대한 bfs
        for elem in connected:  # 5
            for i in range(1, V + 1):
                if m[i][elem] == 1:     # 1, 8
                    if visited[i] == 1 and visited[elem] == 0:
                        visited[elem] = 1
                        if elem not in res:
                            res.append(elem)
                        if elem not in que:
                            que.append(elem)


T = 10
for tc in range(T):
    V, E = map(int, input().split())
    nums = list(map(int, input().split()))

    edges = []
    for i in range(0, len(nums), 2):
        edge = [nums[i], nums[i + 1]]
        edges.append(edge)
    # print(edges)
    edge_mat = [[0] * (V + 1) for _ in range(V + 1)]
    for edge in edges:
        edge_mat[edge[0]][edge[1]] = 1
    # for row in edge_mat:
        # print(*row)

    visited = [1] + [0] * V
    res = []
    process(edges, edge_mat)
    if len(res) != V or 0 in visited:
        print(len(res), V)
    else:
        print(f'#{tc + 1}', *res)
