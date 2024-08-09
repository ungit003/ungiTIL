# def make_head(x, start, end):
#     global route, stack
#     for elem in x:
#         if elem[0] == start:
#             route.append(elem)
#             stack.add(elem[1])
#             break
#
#     if end in stack:
#         return 1
#     elif len(stack) == 0:
#         return 0
#     else:
#         return make_body(x, start, end)
#
#
# def make_body(x, start, end):
#     global route, stack
#     check_stack = len(stack)
#     for elem in x:
#         if elem[0] == route[-1][1]:
#             route.append(elem)
#             stack.add(elem[1])

def find_route(x, start, end):
    route = []
    for elem in x:
        if elem[0] == start:
            route.append(elem)
            if len(route) > 1:
                route.pop()

    start_list = []
    for i in range(len(nums)):
        start_list.append(nums[i][0])

    while route[-1][1] in start_list:
        for elem in x:
            if elem[0] == route[-1][1]:
                route.append(elem)

    if len(route) == 0:
        return 0
    if len(route) == 1:
        if route[0][1] == G:
            return 1
        x.remove(route[0])
        return find_route(x, start, end)

    end_list = []
    for i in range(len(route)):
        end_list.append(route[i][1])
    if G in end_list:
        return 1
    else:
        if route[-1][1] != end:
            x.remove(route[-1])
            return find_route(x, start, end)
    if route[-1][1] == end:
        return 1


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    print(f'#{tc+1}', find_route(nums, S, G))
