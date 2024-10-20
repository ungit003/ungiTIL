T = int(input())
for tc in range(T):
    N, K = map(int, input().split())

    nums = list(range(1, 13))

    ans = 0
    for i in range(1 << 12):
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(nums[j])
        if len(subset) == N and sum(subset) == K:
            ans += 1

    print(f'#{tc+1} {ans}')
