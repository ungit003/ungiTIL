T = 10
for _ in range(T):
    tc = int(input())
    nums = list(map(int, input().split()))

    # i = 0
    # while i < 6:
    #     front = nums.pop(0)
    #     print(i)
    #     nums.append(front - i)
    #
    #     i += 1
    #     print(i)
    #     print(nums)

    i_list = [1, 2, 3, 4, 5]
    i = 0
    while True:
        print(i)
        rear = nums[-1]
        if rear <= 0:
            nums.pop()
            nums.append(0)
            print(nums)
            break
        front = nums.pop(0)
        decrease = i_list[i % 5]
        print(decrease)
        nums.append(front - decrease)
        i += 1
        print(nums)

    print(f'#{tc}', *nums)