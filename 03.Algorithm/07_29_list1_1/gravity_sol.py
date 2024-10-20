# T = int(input())
#
# for _ in range(T) :
#     N = int(input())
#     nums = list(map(int, input().split()))
#     num_dict = {}
#     for i in range(N) :
#         num_dict[i] = nums[i]
#
#     cal_numbers = 0
#
#     max_list = []
#     max_value = max(num_dict.values())
#     for key, value in num_dict.items() :
#         if value == max_value :
#             max_list.append(key)
#     num_of_max = len(max_list)
#     cal_numbers += N - max_list[0] - num_of_max
#
#     print(cal_numbers)
# 값을 받아서 딕셔너리로 만듦
# 키를 모으는데, 밸류가 0이 아닌 것으로만 모아서 만듦
T = int(input())
for tc in range(T):
    N = int(input())
    col = list(map(int, input().split()))
    move_list = []
    for i in range(N):
        blocking = 0
        for j in range(i, N):
            if col[i] <= col[j]:
                blocking += 1
        count = N - i - blocking
        move_list.append(count)
    ans = max(move_list)
    print(f'#{tc+1} {ans}')
