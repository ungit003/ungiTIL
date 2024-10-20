# def finder(arr):
#     global cnt
#     now = [0, 0]
#     while True:
#         if now == [N-1, M-1]:
#             break
#         for elem in d:
#             di, dj = now[0] + d[0], now[1] + d[1]
#             if not(0<=di<N and 0<=dj<M):
#                 continue



# N, M = map(int, input().split())
# mat = [list(map(int, input())) for _ in range(N)]

# d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# cnt = 1
# finder(mat)
# print(cnt)

from collections import deque

def bfs(matrix, n, m):
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 방문 여부를 저장하는 3차원 리스트 (행, 열, 벽 부숨 여부)
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    
    # 시작점 (x, y, 벽 부숨 여부, 거리)
    queue = deque([(0, 0, 0, 1)])  # (0, 0)에서 시작, 거리 1
    visited[0][0][0] = True  # (0, 0) 위치에서 벽을 부수지 않은 상태로 방문
    
    while queue:
        x, y, broke, dist = queue.popleft()
        
        # 도착점에 도달하면 거리 반환
        if x == n - 1 and y == m - 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:  # 범위 체크
                if matrix[nx][ny] == 0 and not visited[nx][ny][broke]:
                    # 이동할 칸이 비어있고, 아직 방문하지 않았다면
                    visited[nx][ny][broke] = True
                    queue.append((nx, ny, broke, dist + 1))
                elif matrix[nx][ny] == 1 and broke == 0 and not visited[nx][ny][1]:
                    # 이동할 칸이 벽이고, 아직 벽을 부수지 않았다면
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))

    return -1  # 도착할 수 없는 경우

# 입력 처리
n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

# BFS 실행
result = bfs(matrix, n, m)
print(result)


'''
from collections import deque

def bfs(matrix, N, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    
    queue = deque([(0, 0, 0, 1)])  # 시작점 (0, 0)에서 거리 1
    visited[0][0][0] = True  # 벽을 부수지 않은 상태로 방문
    
    while queue:
        x, y, broke, dist = queue.popleft()
        
        if x == N - 1 and y == M - 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:  # 범위 체크
                if matrix[nx][ny] == 0 and not visited[nx][ny][broke]:
                    visited[nx][ny][broke] = True
                    queue.append((nx, ny, broke, dist + 1))
                elif matrix[nx][ny] == 1 and broke == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))

    return -1  # 도착할 수 없는 경우

# 입력 처리
N, M = map(int, input("행과 열의 크기를 입력하세요 (예: 4 4): ").split())
matrix = [list(map(int, input().strip())) for _ in range(N)]

while True:
    # 현재 맵 출력
    for row in matrix:
        print(' '.join(map(str, row)))

    # 경로 탐색
    result = bfs(matrix, N, M)
    print("최단 경로 길이:", result)

    # 맵 변경 입력 처리
    change_row = int(input("변경할 행을 입력하세요 (-1 종료): "))
    if change_row == -1:
        break
    change_col = int(input("변경할 열을 입력하세요: "))
    new_value = int(input("새로운 값 (0 또는 1)을 입력하세요: "))
    matrix[change_row][change_col] = new_value  # 맵 업데이트
'''