T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for _ in range(M):
        nums.append(nums.pop(0))

    print(f"#{tc+1} {nums[0]}")