# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
for i in range(1<<n):
    arr_list = []
    for j in range(n):
        if i & (1<<j):
            arr_list.append(arr[j])
    print(arr_list)
    print()
