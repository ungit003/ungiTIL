T = int(input())
for tc in range(T):
    nums = list(map(int, input().split()))

    sumsets = []
    subsets = []
    for i in range(1 << 10):
        subset = []
        for j in range(10):
            if i & (1 << j):
                subset.append(nums[j])
        subsets.append(subset)
        sumset = sum(subset)
        sumsets.append(sumset)

    if sumsets.count(0) > 1:
        print(f'#{tc + 1}', 1)
    else:
        print(f'#{tc + 1}', 0)
