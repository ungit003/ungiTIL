# def sep(x, a):
#     # stt = x[0][0]
#     # end = x[-1][0]
#     # if end == stt:
#     #     a.append(stt)
#     # elif end - stt == 1:
#     #     a.append([stt, end])
#     # elif end - stt > 1:
#     #     mid = (stt + end) // 2
#     #     x_f = x[:mid]
#     #     x_b = x[mid:]
#     #     return sep(x_f, a), sep(x_b, a)
#     if len(x) == 1 or len(x) == 2:
#         a.append(x)
#     else:
#         stt = x[0][0]
#         end = x[-1][0]
#         mid = (stt + end) // 2
#         x_f = [item for item in x if item[0] <= mid]
#         x_b = [item for item in x if item[0] > mid]
#         return sep(x_f, a), sep(x_b, a)
#
#
# # def tour(x):
# #     if len(x) == 1:
# #         fight(x[0])
# #         return x[0][1]
# #     else:
# #         cnt = [len(elem) for elem in x]
# #
# #         if 2 in cnt:
# #             for elem in x:
# #                 if len(elem) == 2:
# #                     fight(elem)
# #             return tour(x)
# #
# #         else:
# #             new_x = []
# #             for i in range(0, len(x), 2):
# #                 elem = x[i] + x[i+1]
# #                 new_x.append(elem)
# #             return tour(new_x)
# def tour(x):
#     if len(x) == 1:
#         fight(x[0])
#         return x[0][1]
#     else:
#         cnt = [len(elem) for elem in x]
#         if 2 in cnt:
#             new_x = []
#             for elem in x:
#                 if len(elem) == 2:
#                     new_x.append(fight(elem))
#                 else:
#                     new_x.append(elem)
#         else:
#             new_x = []
#             for i in range(0, len(x), 2):
#                 if i + 1 < len(x):
#                     new_x.append(fight([x[i], x[i+1]]))
#         return tour(new_x)
#
#
# def fight(x):
#     a = x[0]
#     b = x[1]
#     if (a[1] - b[1]) % 3 == 0 or (a[1] - b[1]) % 3 == 1:
#         return a
#     else:
#         return b
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     nums = list(enumerate((map(int, input().split())), start=1))
#     print(len(nums), nums)
#
#     groups = []
#
#     sep(nums, groups)
#     print(groups)
#
#     res = tour(groups)
#     print(res)


def sep(x, a):
    if len(x) <= 2:
        a.append(x)
    else:
        stt = x[0][0]
        end = x[-1][0]
        mid = (stt + end) // 2
        x_f = [item for item in x if item[0] <= mid]
        x_b = [item for item in x if item[0] > mid]
        sep(x_f, a)
        sep(x_b, a)

def tour(x):
    if len(x) == 1:
        return x[0][1]
    else:
        cnt = [len(elem) for elem in x]
        if 2 in cnt:
            new_x = []
            for elem in x:
                if len(elem) == 2:
                    result = fight(elem)
                    new_x.append(result)
                else:
                    new_x.append(elem)
            return tour(new_x)
        else:
            new_x = []
            for i in range(0, len(x), 2):
                if i + 1 < len(x):
                    result = fight([x[i], x[i+1]])
                    new_x.append(result)
            return tour(new_x)

def fight(x):
    if len(x) == 1:
        return x[0]
    a, b = x
    if (a[1] - b[1]) % 3 == 0 or (a[1] - b[1]) % 3 == 1:
        return a
    else:
        return b

T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(enumerate(map(int, input().split()), start=1))
    print(len(nums), nums)

    groups = []

    sep(nums, groups)
    print(groups)

    res = tour(groups)
    print(res)
