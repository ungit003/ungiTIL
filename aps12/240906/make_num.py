# from collections import deque
#
#
# def filling(c, arr, lev, end):
#     if lev == end:
#         cases.append(arr[:])
#         return
#
#     for i in range(lev, N - 1):
#         if not arr[i]:
#             arr[i] = c
#             filling(c, arr, lev + 1, end)
#             arr[i] = 0
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     ope = list(map(int, input().split()))
#     nums = list(map(int, input().split()))
#
#     cases = deque()
#     blk = [0] * (N - 1)
#     filling('+', blk, 0, ope[0])
#     for i in range(len(cases)):
#         blk2 = cases.popleft()
#         filling('-', blk2, 0, ope[1])
#     for i in range(len(cases)):
#         blk3 = cases.popleft()
#         filling('*', blk3, 0, ope[2])
#     for i in range(len(cases)):
#         blk4 = cases.popleft()
#         filling('/', blk4, 0, ope[3])
#
#     print(cases)
#
#     min_v = float('inf')
#     max_v = float('-inf')
#     for elem in cases:
#         ans = nums[0]
#         for i in range(N - 1):
#             if elem[i] == '+':
#                 ans += nums[i + 1]
#             elif elem[i] == '-':
#                 ans -= nums[i + 1]
#             elif elem[i] == '*':
#                 ans *= nums[i + 1]
#             else:
#                 ans //= nums[i + 1]
#                 if ans < 0 and ans % nums[i + 1]:
#                     ans += 1
#
#         if min_v > ans:
#             min_v = ans
#         if max_v < ans:
#             max_v = ans
#
#     print(f'#{tc+1} {max_v - min_v}')


# def filling(c, arr, lev, end):
#     if lev == end:
#         cases.append(arr[:])
#         return
#
#     for i in range(lev, N - 1):
#         if not arr[i]:
#             arr[i] = c
#             filling(c, arr, lev + 1, end)
#             arr[i] = 0
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     ope = list(map(int, input().split()))
#     nums = list(map(int, input().split()))
#
#     cases = []
#     blk = [0] * (N - 1)
#     filling('+', blk, 0, ope[0])
#     for i in range(len(cases)):
#         blk2 = cases.pop(0)
#         filling('-', blk2, 0, ope[1])
#     for i in range(len(cases)):
#         blk3 = cases.pop(0)
#         filling('*', blk3, 0, ope[2])
#     for i in range(len(cases)):
#         blk4 = cases.pop(0)
#         filling('/', blk4, 0, ope[3])
#
#     min_v = 100000000
#     max_v = -100000000
#     for elem in cases:
#         ans = nums[0]
#         for i in range(N - 1):
#             if elem[i] == '+':
#                 ans += nums[i + 1]
#             elif elem[i] == '-':
#                 ans -= nums[i + 1]
#             elif elem[i] == '*':
#                 ans *= nums[i + 1]
#             else:
#                 ans //= nums[i + 1]
#                 if ans < 0:
#                     ans += 1
#
#         if min_v > ans:
#             min_v = ans
#         if max_v < ans:
#             max_v = ans
#
#     print(f'#{tc+1} {max_v - min_v}')


def cal(lev):
    global temp
    if lev == N - 1:
        ans.append(temp)
        return

    for i in range(4):
        if not ope[i]:
            continue

        ope[i] -= 1
        temp2 = temp
        if i == 0:
            temp += nums[lev + 1]
        if i == 1:
            temp -= nums[lev + 1]
        if i == 2:
            temp *= nums[lev + 1]
        if i == 3:
            # temp = int(temp / nums[lev + 1])
            temp //= nums[lev + 1]
            if temp < 0 and temp2 % nums[lev + 1]:
                temp += 1

        cal(lev + 1)
        temp = temp2
        ope[i] += 1


T = int(input())
for tc in range(T):
    N = int(input())
    ope = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    temp = nums[0]
    ans = []
    cal(0)

    print(f'#{tc+1} {max(ans) - min(ans)}')
