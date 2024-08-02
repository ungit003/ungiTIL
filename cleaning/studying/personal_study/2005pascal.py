# N = int(input())
# pascal = []
# if N > 0 :
#     pascal.append([1])
# for i in range(1, N) :
#     for j in range(1, N) :
#         p
#         piece = pascal[i-1][j-1]
#     pascal.append(piece)
# print(pascal)

N = int(input())
pascal = [[1]]
for i in range(1, N) : # 가로줄 갯수 (2번째부터)
    piece = []
    for j in range(0, i+1) : # 줄당 원소 갯수
        piece.append(1)
    pascal.append(piece)

if N > 2 :
    for i in range(2, N) :
        for j in range(0, i-1) :
            pascal[i][j+1] = pascal[i-1][j] + pascal[i-1][j+1]
for row in pascal :
    print(*row)
# print(pascal)
