# def color_change(info, color, count, stack, floor):
#     if floor > N - 1:
#         return count
#     stack.append(M - info[floor][color])
#     count += M - info[floor][color]
#
#     floor += 1
#     # 위가 흰색
#     if color == 0:
#         if floor < N - 2:
#             color_change(info, 0, count, stack, floor)
#             color_change(info, 1, count, stack, floor)
#         else:
#             color_change(info, 1, count, stack, floor)
#
#     # 위가 파란색
#     if color == 1:
#         if floor < N - 1:
#             color_change(info, 1, count, stack, floor)
#             color_change(info, 2, count, stack, floor)
#         else:
#             color_change(info, 2, count, stack, floor)
#
#     # 위가 빨간색
#     if color == 2:
#         color_change(info, 2, count, stack, floor)
#
#
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     flag = [[s for s in input()] for _ in range(N)]
#
#     for row in flag:
#         print(row)
#
#     count_color = []    # W, B, R
#     for row in flag:
#         colors = [0, 0, 0]
#         for i in row:
#             if i == 'W':
#                 colors[0] += 1
#             elif i == 'B':
#                 colors[1] += 1
#             else:
#                 colors[2] += 1
#         count_color.append(colors)
#
#     for row in count_color:
#         print(row)
#
#     print('-' * 100)
#     stack = []
#     res_list = []
#     res = color_change(count_color, 0, 0, stack, 0)
#     res_list.append(res)
#     print(res_list)


# cnt_change_color = 0
# upper_color = 0
# print(count_color[0])
# cnt_change_color += M - count_color[0][0]
# print(cnt_change_color)
# for i in range(1, N-1):
#     if upper_color == 0:
#         print(count_color[i], upper_color)
#         if count_color[i][0] >= M - count_color[i][0]:
#             cnt_change_color += M - count_color[i][0]
#         elif count_color[i][1] < M - count_color[i][1]:
#             cnt_change_color += M - count_color[i][1]
#             upper_color += 1
#         print(cnt_change_color, upper_color)
#     elif upper_color == 1:
#         print(count_color[i], upper_color)
#         if count_color[i][1] >= M - count_color[i][1]:
#             cnt_change_color += M - count_color[i][1]
#         elif count_color[i][2] < M - count_color[i][2]:
#             cnt_change_color += M - count_color[i][2]
#             upper_color += 2
#         print(cnt_change_color, upper_color)
#     else:
#         print(count_color[i], upper_color)
#         cnt_change_color += M - count_color[i][2]
#         print(cnt_change_color)
# print(count_color[N-1])
# cnt_change_color += M - count_color[N-1][2]
# print(cnt_change_color)
#
# print(f'#{tc+1}', cnt_change_color)


def min_repaint_cost(flag, N, M):
    INF = float('inf')

    # Calculate the cost to paint each row to white, blue, or red
    cost = [[0] * 3 for _ in range(N)]

    for i in range(N):
        cost[i][0] = sum(1 for j in range(M) if flag[i][j] != 'W')
        cost[i][1] = sum(1 for j in range(M) if flag[i][j] != 'B')
        cost[i][2] = sum(1 for j in range(M) if flag[i][j] != 'R')

    # Prefix sums for fast range queries
    prefix_cost = [[0] * 3 for _ in range(N + 1)]

    for i in range(N):
        for c in range(3):
            prefix_cost[i + 1][c] = prefix_cost[i][c] + cost[i][c]

    def calculate_cost(start, end, color):
        return prefix_cost[end][color] - prefix_cost[start][color]

    min_cost = INF

    # Try all possible divisions
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            cost = (
                    calculate_cost(0, i, 0) +  # White section
                    calculate_cost(i, j, 1) +  # Blue section
                    calculate_cost(j, N, 2)  # Red section
            )
            min_cost = min(min_cost, cost)

    return min_cost


T = int(input().strip())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    flag = [input().strip() for _ in range(N)]
    results = []
    min_cost = min_repaint_cost(flag, N, M)
    results.append(f"#{t} {min_cost}")

    print("\n".join(results))