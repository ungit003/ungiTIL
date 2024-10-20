""""""


# def make_seq(s):
#     global ans
#     if sum(stack) == K:
#         print(stack)
#         ans += 1
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             stack.append(arr[i])
#             visited[i] = 1
#             make_seq(i)
#             visited[i] = 0
#             stack.pop()
#
#
# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     ans = 0
#     stack = []
#     visited = [0] * N
#     for i in range(N):
#         stack.append(arr[i])
#         visited[i] = 1
#         make_seq(i)
#         visited[i] = 0
#         stack.pop()
#
#     print(f'#{tc+1}', ans//2)


# def make_seq():
#     global ans
#     if sum(stack) == K:
#         print(stack)
#         ans += 1
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             stack.append(arr[i])
#             visited[i] = 1
#             make_seq()
#             visited[i] = 0
#             stack.pop()
#
#
# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     ans = 0
#     stack = []
#     visited = [0] * N
#     make_seq()
#
#     print(f'#{tc+1}', ans//2)


'''
이렇게 짜면. stack, visited 에 등록할 때와 삭제할 때 순서가 다름. 그래서 이상하게 나옴.
def make_seq():
    global ans
    stack.sort()
    sum_s = sum([x[1] for x in stack])
    if sum_s == K:
        print('K', stack, visited)
        print()
        ans += 1
        return

    for i in range(N):
        if not visited[i]:
            stack.append((i, arr[i]))
            visited[i] = 1
            print(stack, visited)
            make_seq()
            visited[i] = 0
            stack.pop()


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 0
    stack = []
    visited = [0] * N
    # stack.append((0, arr[0]))
    # visited[0] = 1
    make_seq()

    print(f'#{tc+1}', ans//2)
'''


# def make_seq():
#     global ans
#     sum_s = sum([x[1] for x in stack])
#     if sum_s == K:
#         stack.sort()
#         res.add(tuple(stack + visited))
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             stack.append((i, arr[i]))
#             visited[i] = 1
#             # print(stack, visited)
#             make_seq()
#             visited[i] = 0
#             stack.pop()
#
#
# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     ans = 0
#     stack = []
#     visited = [0] * N
#     res = set()
#     # stack.append((0, arr[0]))
#     # visited[0] = 1
#     make_seq()
#
#     print(res)
#     print(f'#{tc + 1}', len(res))
#     # print(f'#{tc+1}', ans//2)

"""
# 얘 왜이럼?
# 0. 함수 정의 = 얕은 복사
def make_seq():
    global ans
    # sum_s = sum([x[1] for x in stack])
    sum_s = sum([arr[i] for i in stack])
    if sum_s == K:                                  # 조건에 맞으면 답에 1 추가하고 리턴
        ans += 1
        '''
        답 체크를 위해서 출력
        '''
        print(stack)
        res.append(stack[:])
        print(res)
        return

    for i in range(N):
        if not visited[i]:                          # 원소에 대해서 방문하지 않았으면 재귀
            stack.append(i)
            visited[i] = 1
            make_seq()
            visited[i] = 0
            stack.pop()


# 1. 입력 받기
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

# 2. 풀이에 필요한 변수 지정하기
    ans = 0
    stack = []
    visited = [0] * N
    res = []
    make_seq()

# 3. 답안 출력하기
    print(ans)
    print(res)
    print(f'#{tc + 1}', len(res))
"""


# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     ans = 0
#     for i in range(1 << N):
#         subset = []
#         check = []
#         for j in range(N):
#             if i & (1 << j):
#                 print(bin(i), bin(j))
#                 subset.append(arr[j])
#                 if sum(subset) == K:
#                     print(subset)
#                     ans += 1
#                     break
#
#     print(f'#{tc+1}', ans)


# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     idx = list(range(N))
#     ans = 0
#     for i in range(1 << N):
#         subset = []
#         for j in range(N):
#             if i & (1 << j):
#                 subset.append(idx[j])
#                 if sum(arr[i] for i in subset) == K:
#                     ans += 1
#                     break
#
#     print(f'#{tc+1}', ans)


# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     idx = list(range(N))
#     subsets = []
#     for i in range(1 << N):
#         subset = []
#         for j in range(N):
#             if i & (1 << j):
#                 subset.append(idx[j])
#         subsets.append(subset)
#
#     ans = 0
#     for sub in subsets:
#         sum_s = 0
#         for i in sub:
#             sum_s += arr[i]
#             if sum_s > K : break
#         if sum_s == K: ans += 1
#
#        # sum_s = sum([arr[i] for i in sub])
#        # if sum_s == K:
#        #     ans += 1
#
#     print(f'#{tc+1}', ans)


# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     ans = 0
#     for i in range(1 << N):
#         subset = []
#         for j in range(N):
#             if i & (1 << j):
#                 subset.append(arr[j])
#         sum_s = 0
#         for i in subset:
#             sum_s += arr[i]
#             if sum_s > K: break
#         if sum_s == K: ans += 1
#
#     print(f'#{tc+1}', ans)


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(1 << N):
        sub = 0
        for j in range(N):
            if i & (1 << j):
                sub += arr[j]
                if sub > K: break
        if K == sub: ans += 1

    print(f'#{tc+1}', ans)
