T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    ans = list(range(1, N+1))
    for i in nums:
        if i in ans:
            ans.remove(i)

    print(f'#{tc+1}', *ans)
