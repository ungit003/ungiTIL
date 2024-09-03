# def change(arr, s, c):
#     if c == cnt:
#         return
#     max_list = []
#     for i in range(len(arr)):
#         if arr[i] == max(arr):
#             max_list.append(i)
#     max_idx = max_list[-1]
#
#     if max_idx == s:
#         change(arr, s+1, c)
#     else:
#         arr[s], arr[max_idx] = arr[max_idx], arr[s]
#         change(arr, s+1, c+1)
def change(arr, inp):
    i, j = inp
    arr[i], arr[j] = arr[j], arr[i]


def cases(lev):
    global max_v
    if lev == cnt:
        val = ''.join(n_list)
        max_v = max(max_v, int(val))
        return
    for elem in subsets:
        change(n_list, elem)
        cases(lev+1)


T = int(input())
for tc in range(T):
    nums, K = map(str, input().split())

    n = len(nums)
    cnt = int(K)
    n_list = []
    for i in range(len(nums)):
        n_list.append(nums[i])

    subsets = []
    for i in range(n):
        for j in range(n):
            if j > i:
                subsets.append((i, j))

    max_v = 0
    cases(0)

    print(f'#{tc+1}', max_v)

