from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    nums = deque(map(int, input().split()))

    for _ in range(M):
        nums.append(nums.popleft())

    print(f'#{tc+1} {nums[0]}')
