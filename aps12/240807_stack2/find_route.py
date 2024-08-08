# def find_route(x):
#     start = 0
#     end = 99
#     route = []
#     # 입력받은 2차원 리스트를 순회합니다
#     for elem in x:
#         # 스타트 기준으로 루트 리스트에 원소를 넣습니다.
#         if elem[0] == start:
#             route.append(elem)
#             print(route)
#             # 스타트를 하나로 제한합니다.
#             if len(route) > 1:
#                 route.pop()
#                 print(route)
#         # 스타트 값이 없으면 0을 반환합니다.
#         if elem[0] == 0 not in x:
#             return 0
#         # 루트에 있는 원소의 끝값과 같은 값으로 시작하는 원소가 있으면 루트에 추가합니다.
#         if elem[0] == route[-1][1]:
#             route.append(elem)
#             print(route)
#     # 루트가 만들어졌을 때, 도달점이 end이면 1을 반환합니다.
#     if route[-1][1] == end:
#         print('end')
#         print(x)
#         return 1
#     # 처음값 말고 루트가 존재하지 않으면, 첫 출발값을 없애고 다시 실행합니다.
#     elif len(route) == 1:
#         x.remove(route[0])
#         print('change')
#         print(x)
#         return find_route(x)
#     # 끝값이 다르면 마지막 원소를 제거하고 다시 실행합니다.
#     else:
#         x.remove(route[-1])
#         print(x)
#         return find_route(x)


# T = 1
# for _ in range(T):
#     # 입력값을 받습니다.
#     tc, N = map(int, input().split())
#     nums = list(map(int, input().split()))

#     # 함수에 넣기 위한 2차원 리스트 모양으로 입력을 바꿉니다.
#     # [[0, 1], [0, 2], [1, 3], ~~~ ]
#     path_list = []
#     for i in range(len(nums)):
#         if i % 2 == 0:
#             path = [nums[i], nums[i+1]]
#             path_list.append(path)
#     # 입력을 편하게 하기 위해서 첫번째 값 기준으로 정렬합니다.
#     path_list.sort()
#     print(path_list)

#     if find_route(path_list) == 1:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')


# no annotation
def find_route(x):
    start = 0
    end = 99
    route = []
    for elem in x:
        if elem[0] == start:
            route.append(elem)
            if len(route) != 1:
                route.pop()
        if elem[0] == route[-1][1]:
            route.append(elem)
        if elem[0] == 0 not in x:
            return 0

    if route[-1][1] == end:
        return 1
    elif len(route) == 1:
        return 0
    else:
        x.remove(route[-1])
        return find_route(x)


T = 10
for _ in range(T):
    tc, N = map(int, input().split())
    nums = list(map(int, input().split()))

    path_list = []
    for i in range(len(nums)):
        if i % 2 == 0:
            path = [nums[i], nums[i+1]]
            path_list.append(path)

    path_list.sort()

    if find_route(path_list) == 1:
        print(f'#{tc} 1')

    else:
        print(f'#{tc} 0')