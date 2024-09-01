"""def inorder(edge):
    if len(ans) == N:
        return
    if len(edge) == 4:
        if visited[edge[int(2)]] == 0:
            inorder(edge[int(2)])
        if visited[edge[int(2)]] == 1 and visited[edge[int(3)]] == 0:
            inorder(edge[int(3)])
        if visited[edge[int(2)]] == 1 and visited[edge[int(3)]] == 1:
            ans.append(edge[1])
            visited[edge[int(0)]] = 1
    if len(edge) == 3:
        if visited[edge[int(2)]]:
            ans.append(edge[1])
            visited[edge[int(0)]] = 1
        else:
            inorder(edge[int(2)])
    if len(edge) == 2:
        ans.append(edge[1])
        visited[edge[int(0)]] = 1


T = 1
for tc in range(T):
    N = int(input())
    edges = [0] + [input().split() for _ in range(N)]

    print(edges)

    ans = []
    visited = [0] * (N + 1)
    inorder(edges[1])
"""


def search(node):
    global result
    if node:    # 노드가 존재하면
        # result += arr[node][1]
        search(arr[node][2])   # 2번 인덱스가 왼쪽 자식
        # 중위 순회이므로 이곳에서 result에 V 를 더해줌
        result += arr[node][1]
        search(arr[node][3])    # 3번 인덱스가 오른쪽 자식
        # result += arr[node][1]


for tc in range(1, 11):     # 총 10개의 TC
    N = int(input())        # 노드의 개수
    arr = [input().split() for _ in range(N)]
    for node_info in arr:
        for idx in range(len(node_info)):
            if node_info[idx].isdecimal():  # 정수로 변환 가능하다면
                node_info[idx] = int(node_info[idx])
    for node_info in arr:
        while len(node_info) != 4:  # 모든 정보가 없다면
            node_info.append(0)     # 자식 없음을 추가
    arr.insert(0, [0, 0, 0, 0])
    result = ''
    search(1)   # 1번 노드부터 순회
    print(f'#{tc} {result}')

