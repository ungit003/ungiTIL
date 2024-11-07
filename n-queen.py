def finder(check, queen):
    global ans
    if check == N * N:
        if queen == N:
            ans += 1
        return
    
    if queen == N:
        # print('ans :', visited)
        ans += 1
        return
    
    for i in range(N):
        for j in range(N): 
            # print('i :', i, '/ j :', j)
            if not visited[i * N + j]:
                visited[i * N + j] += 1
                check += 1
                # print('visited :', visited)
                queen += 1
                # print('q + 1 =', queen)
                nums, plus = cnt_paint(i, j)
                print((i, j), nums)
                print(visited)
                for num in nums: visited[num] += 1
                check += plus
                
                finder(check, queen)
                
                check -= plus
                for num in nums: visited[num] -= 1
                queen -= 1
                check -= 1
                visited[i * N + j] -= 1


def cnt_paint(x, y):
    후보 = []
    갯수 = 0
    # 가로
    for j in range(N):
        if not visited[x * N + j]:
            후보.append(x * N + j)
            갯수 += 1
            
    # 세로
    for i in range(N):
        if not visited[i * N + y]:
            후보.append(i * N + y)
            갯수 += 1
            
    # 대각선
    d = { 'UR': (-1, 1), 'DR': (1, 1), 'UL': (-1, -1), 'DL': (1, -1)}
    for elem in d:
        i = 1
        while True:
            dx, dy = x + d[elem][0] * i, y + d[elem][1] * i
            if not (0 <= dx < N) or not (0 <= dy < N):
                break
            pit = dx * N + dy
            if pit >= N * N:
                break
            if not visited[pit]:
                후보.append(pit)
                갯수 += 1
            i += 1
    return 후보, 갯수

N = int(input())

visited = [0] * N * N
ans = 0
nfac = 1
for i in range(1, N + 1):
    nfac *= i
finder(0, 0)
print(ans / nfac)


# def painting(x, y):
#     print(x, y)
#     plus = 0
#     # 가로
#     for j in range(N):
#         if not visited[x * N + j]:
#             visited[x * N + j] += 1
#             plus += 1
        
#     # 세로
#     for i in range(N):
#         if not visited[i * N + y]:
#             visited[i * N + y] += 1
#             plus += 1
            
#     # 대각선
#     d = { 'UR': (-1, 1), 'DR': (1, 1), 'UL': (-1, -1), 'DL': (1, -1)}
#     for elem in d:
#         i = 1
#         while True:
#             dx, dy = x + d[elem][0] * i, y + d[elem][1] * i
#             pit = dx * N + dy
#             if not (0 <= dx < N) or not (0 <= dy < N):
#                 break
#             if pit >= N * N:
#                 break
#             if not visited[pit]:
#                 visited[pit] += 1
#                 plus += 1
#             i += 1 
#     # print('plus :', plus)
#     return plus