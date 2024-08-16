import sys
sys.stdin = open("input_boong_bread.txt", "r")

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)

    result = 'Possible'
    time = 1
    b_bread = 0
    while True:
        if len(nums) == 0:
            break
        if time > nums[0]:
            result = 'Impossible'
            break
        if time % M == 0:
            b_bread += K
        if time in nums:
            sell = nums.count(time)
            b_bread -= sell
            if b_bread < 0:
                result = 'Impossible'
            for i in range(sell):
                nums.pop()
        time += 1

    print(f'#{tc+1}', result)
