# def make_path(x):
#     check_list = [1]
#     way = []
#     while len(check_list) < V:
#         judge = []
#         for elem in x:
#             if elem[0] == check_list[-1]:
#                 judge.append(elem)
#                 print(judge)
#                 if elem[1] in check_list:
#                     judge.pop()
#                     print(judge)
#         print('-' * 100)
#
#         if len(judge) == 0:
#             for elem in x:
#                 if elem[0] == check_list[-2]:
#                     judge.append(elem)
#                     if elem[1] in check_list:
#                         judge.pop()
#                     print(judge)
#
#         min_value = judge[0][1]
#         min_jud = judge[0]
#         for i in range(len(judge)):
#             if judge[i][1] < min_value:
#                 min_value = judge[i][1]
#                 min_jud = judge[0]
#         way.append(min_jud)
#         check_list.append(min_value)
#         print(check_list)
#         print('^' * 100)
#     return check_list
#
#
# T = 1
# for tc in range(T):
#     V, E = map(int, input().split())
#     nums = list(map(int, input().split()))
#
#     path_list = []
#     for i in range(len(nums)):
#         if i % 2 == 0:
#             path_list.append([nums[i], nums[i+1]])
#             path_list.append([nums[i+1], nums[i]])
#     print(path_list)
#
#     # print(make_path(path_list))
#     ans = map(str, make_path(path_list))
#     res = '-'.join(ans)
#     print(f'#{tc+1}', res)

# 강의
def DFS(s, V):              # s시작정점, V 정점개수(1번부터인 정점의 마지막정점)
    visited = [0]*(V+1)     # 방문한 정점을 표시
    stack = []              # 스택생성
    print(s)
    visited[s] = 1          # 시작정점 방문표시
    v = s
    while True:
        for w in adjL[v]:       # v에 인접하고, 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)  # push(v) 현재 정점을 push하고
                v = w            # w에 방문
                print(v)
                visited[w] = 1     # w에 방문 표시
                break           # for w, v부터 다시 탐색
        else:                   # 남은 인접정점이 없어서 break가 걸리지 않은경우
            if stack:   # 이전 갈림길을 스택에서 꺼내서... if TOP > -1
                v = stack.pop()
            else:       # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색종료
                break   # while True:



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    print(adjL)
    arr = list(map(int, input().split()))
    print(arr)
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
        print(adjL)

    DFS(1, V)
