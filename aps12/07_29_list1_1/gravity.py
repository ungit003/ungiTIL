T = int(input())
for i in range(T) :
    ans = 0
    N = int(input())
    nums = list(map(int, input().split()))
    for j in range(N) :
        if nums[j] == 0 :
            ans += N - j
