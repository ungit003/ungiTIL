"""
풀이 전략
1. 전체를 순회하면서 최고값을 찾고, 리스트를 만든다.
2. 리스트의 값을 시작으로 델타 탐색을 한다. 현재 위치보다 더 낮은 곳으로만 연결할 수 있다.
3. 공사를 했다 안했다를 플래그로 지정한다. 만약 공사를 하지 않았다면, 자신보다 높거나 같은 곳에 대해서 k만큼 깎을 수 있다.
깎았을 때 자신보다 낮으면 델타탐색 가능.
4. 델타탐색을 하면서 한 칸 움직일 때 마다 로드값을 +1 한다.
5. dfs?
"""


def find_route(x, y, l):
    for k in range(4):
        dx, dy = x + d[k][0], y + d[k][1]
        if 0 <= dx < N and 0 <= dy < N:
            if mount[dx][dy] < mount[x][y]:
                l += 1
                print(dx,dy, l)
                return find_route(dx, dy, l)
    return l


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    mount = [list(map(int, input().split())) for _ in range(N)]

    top_list = []
    for i in range(N):
        for j in range(N):
            if len(top_list) == 0:
                top_list.append([mount[i][j], i, j])
            else:
                if mount[i][j] > top_list[0][0]:
                    top_list.clear()
                    top_list.append([mount[i][j], i, j])
                elif mount[i][j] == top_list[0][0]:
                    top_list.append([mount[i][j], i, j])

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    l_list = []
    for i in range(len(top_list)):
        l_list.append(find_route(top_list[i][1], top_list[i][2], 1))
    print(l_list)