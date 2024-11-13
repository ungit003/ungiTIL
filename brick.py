# '''
# 1. 전체 벽돌 갯수 카운트
# 2. finder = dfs
# 3. 부순 벽돌 카운트
#     1. 로테이션 순회
#     2. 부수는 함수
#     3. 백트래킹
# 4. bricks - finder = ans

# '''
# from collections import deque
# import copy


# def breaker(now=0):                 # 부수는 함수
#     break_cnt = 0                   # 부순 갯수
#     global broken                   # 부순거 밖에다 더해줄거임
#     def breaking(x):                                                        # !!!!!함수 접어뒀다가 나중에 와서 보는거 권장!!!!!
#         break_cnt = 0                                                       # 부순거 세는거
#         brick_number = 0                                                    # 0이 아닌 브릭 위치
#         i = 0
#         while True:                                                         # 브릭 위치 찾는 while문
#             if mat[i][x]:
#                 brick_number = mat[i][x]
#                 break
#             i += 1

#         if brick_number > 1:                                                # 브릭값이 1보다 클 때 bfs 돌림
#             d = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}          # 4방향 기준 델타
#             break_list = deque()
#             break_list.append((i, x, brick_number))
#             while break_list:                                               
#                 brick = break_list.popleft()    
#                 if brick[2] == 1:                                           # 브릭값 1이면 0으로 바꾸고, 부순 수 +1,  패스
#                     break_cnt += 1
#                     mat[i][x] = 0
#                     continue
#                 if brick[2] > 1:                                            # 브릭값 1 초과면 델타 돌려서 덱이 넣기
#                     for elem in d:
#                         for b in range(1, brick_number+1):
#                             di, dj = i + d[elem][0] * b, x +d[elem][1] * b
#                             if not(0 <= di < H) or (0 <= dj < W):
#                                 continue
#                             brick = (di, dj, mat[di][dj])
#                             if brick[2] >= 1:                           
#                                 break_list.append(brick)
        
#         flag = False                                                        # 열에 공백 생겼으면 플래그 true로 바뀜
#         for j in range(W):                                                  # 열 확인하는거, 숫자만 모으는거 리스트 따로 맹금
#             check_column = []
#             change_column = []
#             for i in range(H):
#                 check_column.append(mat[i][j])
#                 if mat[i][j]:
#                     change_column.append(mat[i][j])
#                 if i:                                                       # i가 0보다 클 때, 바로 앞꺼랑 비교해서 0이 껴있으면 플래그 true
#                     if check_column[i-1] - check_column[i] < 0:
#                         flag = True
#             if flag:                                                        # 체인지 컬럼 들고와서 값 바꾸는애
#                 while True:                                                 # 0보다 큰애만 담아서 모자란만큼 0 추가
#                     if len(change_column) == H:
#                         break
#                     change_column.append(0)
#                 for i in range(H):                                          # 값 변경
#                     if mat[i][j] != change_column[i]:
#                         mat[i][j] = change_column[i]
#                 flag =False
#         return break_cnt

#     if now == N+1:                  # dfs 탈출 조건. N번 뿌시고 돌아와서 N+1이 되면 탈출
#         return
    
#     new_mat = copy.deepcopy(mat)    # dfs 구문
#     for col in range(W):
#         break_cnt += breaking(col)
#         breaker(now+1)
#         mat = new_mat

#     broken += break_cnt



# def count_brick():                  # 최초 벽돌 세는 함수
#     cnt = 0
#     for i in range(H):
#         for j in range(W):
#             if mat[i][j]:
#                 cnt += 1
#     return cnt
                

# # 1. 입력값 받기
# T = int(input())
# for tc in range(T):
#     N, W, H = map(int, input().split())
#     mat = [list(map(int, input().split())) for _ in range(H)]

# # 풀이를 위한 기초 로직
#     bricks = count_brick()          # 일단 전체 벽돌 갯수를 센다
#     broken = 0
#     breaker()
#     ans = bricks - broken        # 전체 벽돌에서 부순거 뺀다
#     print(f'#{tc+1} {ans}')         # 답 출력한다다



from collections import deque
import copy

def breaking(x):
    global mat
    break_cnt = 0
    brick_number = 0
    i = 0
    while i < H:
        if mat[i][x]:
            brick_number = mat[i][x]
            break
        i += 1
    
    if brick_number == 0:
        return break_cnt

    d = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
    break_list = deque()
    break_list.append((i, x, brick_number))
    
    while break_list:
        brick = break_list.popleft()
        di, dj = brick[0], brick[1]
        if brick[2] == 1:
            break_cnt += 1
            mat[di][dj] = 0
            continue
        
        for direction in d.values():
            for b in range(1, brick[2]):
                ni, nj = di + direction[0] * b, dj + direction[1] * b
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                if mat[ni][nj] > 0:
                    break_list.append((ni, nj, mat[ni][nj]))
                    mat[ni][nj] = 0

    return break_cnt

def collapse_columns():
    global mat
    for j in range(W):
        non_zero_bricks = [mat[i][j] for i in range(H) if mat[i][j] > 0]
        for i in range(H - len(non_zero_bricks)):
            mat[i][j] = 0
        for i in range(len(non_zero_bricks)):
            mat[H - len(non_zero_bricks) + i][j] = non_zero_bricks[i]

def breaker(now=0):
    global broken, mat

    if now == N:
        return

    new_mat = copy.deepcopy(mat)
    for col in range(W):
        break_cnt = breaking(col)
        collapse_columns()
        broken += break_cnt
        breaker(now + 1)
        mat = copy.deepcopy(new_mat)

def count_brick():
    cnt = 0
    for i in range(H):
        for j in range(W):
            if mat[i][j]:
                cnt += 1
    return cnt

T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(H)]

# 풀이를 위한 기초 로직 
bricks = count_brick()  
broken = 0  
breaker()  
ans = bricks - broken  
print(f'#{tc+1} {ans}')