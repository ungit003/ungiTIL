T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    # print(N, Q)
    nums = [list(map(int, input().split()))for _ in range(Q)]
    # print(nums)

    boxes = [0] * N
    for i in range(Q):
        for j in range(nums[i][0], nums[i][1]+1):
            boxes[j-1] = i+1
            # print(boxes)

    print(f'#{tc+1}', *boxes)
