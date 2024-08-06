'''

'''
for tc in range(10):
    dump = int(input())
    nums = list(map(int, input().split()))
    avg = sum(nums)//100

    nums_dict = {}
    for i in range(100):
        nums_dict[i] = nums[i]

    count = 0
    while count < dump:
        if max(nums_dict.values()) - min(nums_dict.values()) == 1 :
            break
        h_list = []
        s_list = []
        for key, value in nums_dict.items():
            if value == max(nums_dict.values()):
                h_list.append(key)
            if value == min(nums_dict.values()):
                s_list.append(key)
        # print(h_list)
        # print(s_list)
        # print('-' * 50)
        nums_dict[h_list[0]] -= 1
        nums_dict[s_list[0]] += 1
        count += 1


    print(f'#{tc+1} {max(nums_dict.values()) - min(nums_dict.values())}')

# print(f'{max(nums_dict.values()) - min(nums_dict.values())}')
#인덱스

# for tc in range(10):
#     dump = int(input())
#     nums = list(map(int, input().split()))
#
#     count = 0
#     while count < dump:
#         max_index = nums.index(max(nums))
#         min_index = nums.index(min(nums))
#         nums[max_index] -= 1
#         nums[min_index] += 1
#         count += 1
#
#     print(f'#{tc+1} {max(nums) - min(nums)}')



# dump = int(input())
# nums = list(map(int, input().split()))
#
# nums_dict = {i: nums[i] for i in range(100)}
#
# count = 0
# while count < dump:
#     max_value = max(nums)
#     min_value = min(nums)
#
#     h_list = [key for key, value in nums_dict.items() if value == max_value]
#     s_list = [key for key, value in nums_dict.items() if value == min_value]
#
#     if not h_list or not s_list:
#         break  # h_list 또는 s_list가 비어 있는 경우 루프 종료
#
#     nums[h_list[0]] -= 1
#     nums[s_list[0]] += 1
#     nums_dict[h_list[0]] = nums[h_list[0]]
#     nums_dict[s_list[0]] = nums[s_list[0]]
#
#     count += 1
#
# print(f'{max(nums) - min(nums)}')
