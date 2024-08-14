# import sys
# sys.stdin = open('input.txt')


def switching(sw, st):  # [~] [1, 2]
    if st[0] == 1:
        for i in range(len(sw)):
            if i % st[1] == st[1] - 1:
                sw[i] = 1 - sw[i]
        # print(sw)

    else:   # [2, 3]
        sw[st[1] - 1] = 1 - sw[st[1] - 1]
        # print(sw, 0)
        i = 1
        while True:
            if st[1] - 1 - i < 0 or st[1] - 1 + i > T - 1:
                # print(st[1] - 1 - i, st[1] - 1 + i, T - 1)
                # print('stop1')
                break
            elif sw[st[1] - 1 - i] == sw[st[1] - 1 + i]:
                sw[st[1] - 1 - i] = 1 - sw[st[1] - 1 - i]
                sw[st[1] - 1 + i] = 1 - sw[st[1] - 1 + i]
                i += 1
                # print(sw, i)
            else:
                # print('stop2')
                break
    return sw


T = int(input())
switch = list(map(int, input().split()))
N = int(input())
student = [list(map(int, input().split())) for _ in range(N)]

# print(switch)
# print(student)

for elem in student:
    switching(switch, elem)

# print(*switch)
if len(switch) > 80:
    print(*switch[:20])
    print(*switch[20:40])
    print(*switch[40:60])
    print(*switch[60:80])
    print(*switch[80:])

if 60 < len(switch) <= 80:
    print(*switch[:20])
    print(*switch[20:40])
    print(*switch[40:60])
    print(*switch[60:])

if 40 < len(switch) <= 60:
    print(*switch[:20])
    print(*switch[20:40])
    print(*switch[40:])

if 20 < len(switch) <= 40:
    print(*switch[:20])
    print(*switch[20:])

if len(switch) < 20:
    print(*switch)

# 하드코딩 말고 20개씩 끊어서 표기하는 법
# for i in range(1, sw_count + 1):
#     print(sw_list[i - 1], end=' ')
#     if i % 20 == 0:
#         print()
