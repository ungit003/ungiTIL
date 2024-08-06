# N = int(input())
# for num in range(N):
#     size = int(input())
#     print(f'#{num + 1}')
#     pascal = []
#     for i in range(0, size):  # 가로줄 갯수 (2번째부터)
#         piece = []
#         for j in range(0, i + 1):  # 줄당 원소 갯수
#             piece.append(1)
#         pascal.append(piece)
#
#     if size > 2:
#         for i in range(2, size):
#             for j in range(0, i - 1):
#                 pascal[i][j + 1] = pascal[i - 1][j] + pascal[i - 1][j + 1]
#     for row in pascal:
#         print(*row)
T = int(input())
for tc in range(T):
    N = int(input())
    pascal = []
    for i in range(N):
        line = [1] * (i+1)
        pascal.append(line)
    # print(pascal)
    if N > 2:
        for i in range(2, N):
            for j in range(i-1):
                pascal[i][j+1] = pascal[i-1][j] + pascal[i-1][j+1]
    print(f'#{tc+1}')
    for row in pascal:
        print(*row)