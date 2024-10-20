# T = int(input())
# for tc in range(T):
#     I, J = list(map(int, input().split()))
#     arr = [[0] * (J+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(I)] + [[0] * (J+2)]
#
#
#     max = 0
#     di = [0, 0, 1, 0, -1]
#     dj = [0, 1, 0, -1, 0]
#
#
#     for i in range(1, I+1):
#         for j in range(1, J+1):
#             shot_list = []
#             for ii in di:
#                 for jj in dj:
#                     shot = arr[i + ii][j + jj]
#                     shot_list.append(shot)
#             print(shot_list)
#             ans = sum(shot_list)
#             if ans > max:
#                 max = ans
#                 print(max)
#
#     # arr.insert(0, [0] * (J+2))
#     # arr.insert(I+1, [0] * (J+2))
#     # shot_list = []
#     # shot = [arr[i][j], arr[i][j+1], arr[i+1][j], arr[i][j-1], arr[i-1][j]]
#
#     print(f'#{tc+1} {max}')

# 입력값을 받고 리스트를 구성할 때 바깥에 0을 한번 둘러줌
T = int(input())
for tc in range(T):
    I, J = list(map(int, input().split()))
    arr = [[0] * (J+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(I)] + [[0] * (J+2)]

# max를 설정하고 풍선이 터지는 범위의 값을 합쳐서 비교함
    max = 0
    for i in range(1, I+1):
        for j in range(1, J+1):
            shot = [arr[i][j], arr[i][j+1], arr[i+1][j], arr[i][j-1], arr[i-1][j]]
            ans = sum(shot)
            if ans > max:
                max = ans

    print(f'#{tc+1} {max}')