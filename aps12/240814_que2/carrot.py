T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split())) + [0]
    # print(nums)

    ans = []
    cnt = 1
    for i in range(N):
        if nums[i] < nums[i+1]:
            cnt += 1
            print(cnt)

        else:
            ans.append(cnt)
            cnt = 1
            print(cnt)

    print(f'#{tc+1}', max(ans))
