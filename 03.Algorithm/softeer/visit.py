"""
풀이 전략
dfs
m개의 점을 방문.
1번 start m번 end
1 -> 2, 2-> 3 ~~~ cnt + 1
만약에 갈 길이 없으면 break
만약에 cnt = m-1 이면 ans + 1

문제가 이상하게 풀림..
그냥 갔던 길을 스택에 쌓는게 더 좋아보이는데.
1. 출발 -> 종착 dfs , 인덱스를 넣는 게 좋을 듯?
2. 중간의 경유지들 인덱스가 차례대로이면, ans + 1

dfs 에서 필요한 것.
visited, stack visited는 mat자체로도 될듯.

dfs 구성 생각해보기.
1. dfs 출발, 도착
만약 출발 = 도착이 되면.
포인트 행렬에 대해서 인덱스를 구함
인덱스 < 인덱스 < 인덱스 이런식으로 구성되면
답 +1

"""


# def find_route(s, e):
#     global cnt, ans
#     if s == e:
#         cnt += 1
#         if cnt == m - 1:
#             ans += 1
#         return
#     for k in range(4):
#         dx, dy = s[0] + d[k][0], s[1] + d[k][1]
#         if not (0 <= dx < n and 0 <= dy < n):
#             continue
#         if not mat[dx][dy]:
#             mat[dx][dy] = 1
#             for row in mat:
#                 print(row)
#             print('-')
#             find_route([dx, dy], e)
#             mat[dx][dy] = 0
#
#
# n, m = map(int, input().split())
# mat = [list(map(int, input().split())) for _ in range(n)]
# points = [list(map(int, input().split()))for _ in range(m)]
# pnt = []
# for i in range(m):
#     pnt.append([points[i][0]-1, points[i][1]-1])
# print(pnt)

# d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# ans = 0
# for i in range(m-1):
#     cnt = 0
#     mat[pnt[i][0]][pnt[i][1]] = 1
#     find_route(pnt[i], pnt[i+1])
# print(ans)

def route_finder(s, e):
    global ans
    if s == e:
        for i in range(1, m-1):
            if pnt[i] not in stack or pnt[i+1] not in stack:
                return
            if stack.index(pnt[i]) >= stack.index(pnt[i+1]):
                return
        ans += 1
        return
    for k in range(4):
        dx, dy = s[0] + d[k][0], s[1] + d[k][1]
        if not (0 <= dx < n and 0 <= dy < n):
            continue
        if mat[dx][dy] == 0:
            stack.append((dx, dy))
            mat[dx][dy] = 1
            # for row in mat:
            #     print(row)
            # print()
            route_finder((dx, dy), e)
            stack.pop()
            mat[dx][dy] = 0


n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
points = [list(map(int, input().split()))for _ in range(m)]
pnt = []
# pnt_idx = {}
for i in range(m):
    pnt.append((points[i][0]-1, points[i][1]-1))
    # pnt_idx[(points[i][0]-1, points[i][1]-1)] = i
print(pnt)
# print(pnt_idx)

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0
stack = []
stack.append(pnt[0])
mat[pnt[0][0]][pnt[0][1]] = 1
route_finder(pnt[0], pnt[-1])
print(ans)

