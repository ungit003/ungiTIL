# 정리
# 주어진 숫자 리스트를 토너먼트 규칙에 맞게 쪼갭니다.
# 쪼갬과 동시에 (카드, 인덱스) 의 튜플로 만들어 줍니다.
def seperator(start, end):
    if start == end:
        t_list.append([(nums[start], start)])
    elif end - start + 1 > 2:
        mid = (start + end) // 2
        return seperator(start, mid), seperator(mid + 1, end)
    else:
        t_list.append([(nums[start], start), (nums[end], end)])


# 두 개의 튜플이 들어왔을 때, 승자를 찾아주는 함수입니다.
def find_winner(x, y):
    a = x[0]
    b = y[0]
    if (a - b) % 3 == 0 or (a - b) % 3 == 1:
        return x
    else:
        return y


# 토너먼트 입니다. 리스트 안에서 둘씩 짝지어져있는 튜플들을 승부시킵니다.
# 이긴 튜플만 남아있습니다.
def tnmt(t_list):
    for i in range(len(t_list)):
        if len(t_list[i]) == 2:
            a = find_winner(t_list[i][0], t_list[i][1])
            t_list[i].clear()
            t_list[i].append(a)

# 승자들을 둘씩 짝지어서 새 리스트를 만듭니다.
    new_t_list = []
    for i in range(len(t_list)):
        if i % 2 == 0:
            a = t_list[i] + t_list[i + 1]
            new_t_list.append(a)

# 결승 전까지 계속 반복시킵니다.
    if len(new_t_list) == 1:
        return new_t_list
    else:
        return tnmt(new_t_list)


# 결승전에서 승자의 인덱스 값을 가져옵니다.
def last(t_list):
    for i in range(len(t_list)):
        if len(t_list[i]) == 2:
            a = find_winner(t_list[i][0], t_list[i][1])
    return a[1]


# 입력을 받습니다.
T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

# 토너먼트 리스트를 만들고, 결과를 출력합니다.
    t_list = []
    seperator(0, N-1)

    res = tnmt(t_list)
    print(f'#{tc+1} {last(res) + 1}')




# def find_winner(x, y):
#     a = x[0]
#     b = y[0]
#     if (a - b) % 3 == 0 or (a - b) % 3 == 1:
#         return x
#     else:
#         return y
#
#
# def seperator(start, end):
#     if start == end:
#         t_list.append([(nums[start], start)])
#     elif end - start + 1 > 2:
#         mid = (start + end) // 2
#         return seperator(start, mid), seperator(mid + 1, end)
#     else:
#         t_list.append([(nums[start], start), (nums[end], end)])
#
#
# def fight(t_list):
#     for i in range(len(t_list)):
#         if len(t_list[i]) == 2:
#             a = find_winner(t_list[i][0], t_list[i][1])
#     return a[1]
#
#
# def assemble(t_list):
#     new_t_list = []
#     for i in range(len(t_list)):
#         if i % 2 == 0:
#             a = t_list[i] + t_list[i + 1]
#             new_t_list.append(a)
#
#
# def tnmt(t_list):
#     for i in range(len(t_list)):
#         if len(t_list[i]) == 2:
#             a = find_winner(t_list[i][0], t_list[i][1])
#             t_list[i].clear()
#             t_list[i].append(a)
#     print(t_list)
#
#     new_t_list = []
#     for i in range(len(t_list)):
#         if i % 2 == 0:
#             a = t_list[i] + t_list[i + 1]
#             new_t_list.append(a)
#     print(new_t_list)
#     if len(new_t_list) == 1:
#         return new_t_list
#     else:
#         return tnmt(new_t_list)
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     nums_dict = {}
#     for i in range(len(nums)):
#         nums_dict[i] = nums[i]
#
#     t_list = []
#     seperator(0, N-1)
#     print(t_list)
#
#     res = tnmt(t_list)
#     ans = fight(res)
#     print(ans)
#
#     print(f'#{tc+1} {fight(res) + 1}')