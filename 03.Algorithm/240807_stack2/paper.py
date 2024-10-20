def papering(x):
    global memo
    if x >= 3:
        memo[x] = papering(x - 1) + papering(x - 2) * 2
    return memo[x]


T = int(input())
for tc in range(T):
    N = int(input()) // 10

    memo = [0] * (N + 1)
    memo[1] = 1
    memo[2] = 3

    print(f'#{tc + 1}', papering(N))

# def papering(x):
#     if x == 1:
#         return 1
#     elif x == 2:
#         return 3
#     else:
#         return papering(x-1) + papering(x-2) * 2
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input()) // 10
#
#     print(f'#{tc+1}', papering(N))
