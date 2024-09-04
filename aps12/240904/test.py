# a = '1DB176C588D26EC'
# b = int(a, 16)
# print(b)
# c= bin(b)
# print(c)
#
# print('0b01110110110001011101101100010110001000110100100110111011')
#
# d = '1DB176C588D26EC'
# e = bin(int(d, 16))
# print(e)

# b_list = []
# for i in range(len(a)):
#     if a[i].isdecimal():
#         b = int(a[i])
#     else:
#         b = hex(int(a[i]))
#     print(b)
#     b_list.append(b)
# print(b_list)

# c_list = []
# for elem in b_list:
#     # c = []
#     # for i in range(1, len(elem)-1):
#     #     c.append(elem[i])
#     #     n_c = ''.join(c)
#     #     c_list.append(n_c)
#     c_list.append(c)
# print(c_list)

a = 1
for i in range(15, 0, -1):
    a *= i
    print(a)

