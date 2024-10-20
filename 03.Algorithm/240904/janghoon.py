'''
문제 요약 : 점원 탑쌓아서 B 이상으로 만들기. (B에 가장 가까운 값) - B 출력.
'''

'''
직원은 한 번만 쌓을 수 있음. -> visited
쌓으면서 B를 넘기면 그 차이를 저장.
'''


def find(s):
    global tall, ans
    if tall >= B:
        ans = min(tall - B, ans)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            tall += nums[i]
            if tall - B > ans:
                visited[i] = 0
                tall -= nums[i]
                break
            find(i)
            visited[i] = 0
            tall -= nums[i]


T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    nums = list(map(int, input().split()))

    visited = [0] * N
    ans = float('inf')
    tall = 0
    for i in range(N):
        visited[i] = 1
        tall += nums[i]
        find(i)
        visited[i] = 0
        tall -= nums[i]
    print(f'#{tc+1}', ans)

# def find(s, current_sum):
#     global ans
#     if current_sum >= B:
#         ans = min(current_sum - B, ans)
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             find(i, current_sum + nums[i])
#             visited[i] = False
#
# T = int(input())
# for tc in range(T):
#     N, B = map(int, input().split())
#     nums = list(map(int, input().split()))
#
#     visited = [False] * N
#     ans = float('inf')  # 시작 시 가장 큰 값을 설정
#
#     for i in range(N):
#         visited[i] = True
#         find(i, nums[i])
#         visited[i] = False
#
#     print(f'#{tc+1}', ans)



