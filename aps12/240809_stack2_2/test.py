# a = [1]
# x = a.pop()
# y = a.pop()
# print(x + y)
# words = [[1, 2], 'b', 'c', 'd']
#
#
# def abc(x):
#     route = []
#     for i in range(len(x)):
#         if x[i] != 0:
#             route.append(x[i])
#
#     x.remove(route[0])
#     return x
#
#
# print(abc(words))
def f(i, N, v):
    if i == N:
        return print('x')
    elif arr[i] == v:
        return print('o')
    else:
        print(arr[i])
        f(i+1, N, v)


arr = [1, 2, 3, 4, 5]

f(0, len(arr), 45)