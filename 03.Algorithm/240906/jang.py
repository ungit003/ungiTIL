""""""

'''
# 순열 + 인덱스
def per(n):
    if len(temp) == n:
        permutations.append(temp[:])
        return
    for i in range(n):
        if i not in temp:
            temp.append(i)
            per(n)
            temp.pop()


T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    nums = list(map(int, input().split()))

    res = 200000
    permutations = []
    temp = []
    per(N)
    # print(permutations)
    # print(len(permutations))
    for elem in permutations:
        ans = 0
        for i in elem:
            ans += nums[i]
            if 0 <= ans - B < res:
                # print(ans)
                res = ans-B
                break

    print(f'#{tc+1}', res)
'''

# 조합 + 인덱스 / 난 못함..
# def com(s, n):
#     if len(temp) == n:
#         combinations.append(temp)
#         return
#
#     for i in range(s, n):
#         if i not in temp:
#             com(s, n)
#
#
# T = int(input())
# for tc in range(T):
#     N, B = map(int, input().split())
#     nums = list(map(int, input().split()))
#
#     res = 200000
#     combinations = []
#     temp = []
#     com(0, N)
#     for elem in combinations:
#         ans = 0
#         for i in elem:
#             ans += nums[i]
#             if 0 <= ans - B < res:
#                 res = ans - B
#                 break
#
#     print(f'#{tc+1}', res)

'''
# dfs
def dfs():
    global ans, stack
    if 0 <= stack - B < ans:
        ans = stack - B
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            stack += nums[i]
            dfs()
            stack -= nums[i]
            visited[i] = 0


T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    nums = list(map(int, input().split()))

    ans = 200000
    visited = [0] * N
    stack = 0
    dfs()

    print(f'#{tc+1}', ans)
'''


# 이게 dfs 가 맞나?
def dfs(s):
    global ans, stack
    if 0 <= stack - B < ans:
        ans = stack - B
        return

    for i in range(s+1, N):
        stack += nums[i]
        dfs(i)
        stack -= nums[i]


T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    nums = list(map(int, input().split()))

    ans = 200000
    stack = 0
    dfs(-1)

    print(f'#{tc+1}', ans)
