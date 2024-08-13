# def rotating(m, rot_info):
#     check_right = m[rot_info[0] - 1][2]
#     check_left = m[rot_info[0] - 1][6]
#     # rotate self
#     if rot_info[1] == 1:
#         m[rot_info[0] - 1].append(m[rot_info[0] - 1].pop(0))
#     else:
#         m[rot_info[0] - 1].insert(0, m[rot_info[0] - 1].pop())
#
#     # rotate right
#     if rot_info[0] < 4 and m[rot_info[1]][6] != check_right:
#         if rot_info[1] == 1:
#             m[rot_info[0]].insert(0, m[rot_info[0]].pop())
#         else:
#             m[rot_info[0]].append(m[rot_info[0]].pop(0))
#
#     # rotate left
#     if rot_info[0] > 1 and m[rot_info[1]][2] != check_left:
#         if rot_info[1] == 1:
#             m[rot_info[0] + 1].insert(0, m[rot_info[0] + 1].pop())
#         else:
#             m[rot_info[0] + 1].append(m[rot_info[0] + 1].pop(0))
#     return m
def rotating(m, num, dor):
    check_right = m[num - 1][2]
    check_left = m[num - 1][6]
    # rotate self
    if dor == 1:
        m[num - 1].append(m[num - 1].pop(0))
    else:
        m[num - 1].insert(0, m[num - 1].pop())

    if num < 4 and m[num][6] != check_right:
        if dor == 1:
            m[]



T = int(input())
for tc in range(T):
    K = int(input())
    mags = []
    for _ in range(4):
        mag = list(map(int, input().split()))
        mags.append(mag)
    rotate = []
    for _ in range(K):
        rot = list(map(int, input().split()))
        rotate.append(rot)

    for row in mags:
        print(row)
    print(rotate)

    for elem in rotate:
        rotating(mags, elem)
        print(elem)
        for row in mags:
            print(row)

    res = []
    for i in range(4):
        res.append(mags[i][0] * 2**i)
    print(res)


