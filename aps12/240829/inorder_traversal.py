"""
중위순회하는 코드 작성
"""
T = 1
for tc in range(T):
    N = int(input())
    nodes = [input().split() for _ in range(N)]

    for node in nodes:
        for i in range(len(node)):
            if node[i].isdecimal():
                node[i] = int(node[i])

    print(nodes)
