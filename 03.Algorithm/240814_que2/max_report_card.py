T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort(reverse=True)
    sum_max = sum(nums[:K])
    print(f'#{tc+1} {sum_max}')
