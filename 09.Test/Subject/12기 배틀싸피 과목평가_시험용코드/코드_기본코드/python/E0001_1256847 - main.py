from libs._bridge import init, submit, close
from collections import deque

NICKNAME = 'main_김주찬'
game_data = init(NICKNAME)

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
# 입력 데이터 분류
direction = ['U', 'R', 'D', 'L']
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
allies = {}  # 아군 정보. 예) allies['A'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])  # 맵의 세로 크기
    map_width = int(header[1])  # 맵의 가로 크기
    num_of_allies = int(header[2])  # 아군의 수
    num_of_enemies = int(header[3])  # 적군의 수
    num_of_codes = int(header[4])  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])


def bfs(my_position, target_position):  # 내 위치, 타겟 위치
    # [x좌표][y좌표][방향]
    visited=[[[False]*4 for _ in range(N)]for _ in range(N)]
    q=deque()
    x,y=my_position
    q.append((x,y,0,[]))  # x좌표, y좌표, 방향, 경로
    visited[x][y][0]=True  # 방문표시

    while q:  # 큐가 비어있지 않는동안 반복
        x,y,d,path=q.popleft()
        nx,ny=x+dx[d],y+dy[d]  # 다음 탐색위치
        
        if [nx,ny]==target_position:
            return path+[(direction[d], 'F')]  # 적 포탑 왔으면 발사 명령어 반환
        
        if 0<=nx<N and 0<=ny<N: # 맵 범위 벗어나면 다음 탐색
            if map_data[nx][ny]=='G' and not visited[nx][ny][d]:  # 다음 탐색위치가 풀이고 방문하지 않았다면
                visited[nx][ny][d]=True  # 방문 표시 후
                q.append((nx, ny, d, path+[(direction[d], 'A')]))  # 방향과 이동명령 경로에 추가하고 큐 넣기
            
            elif 'E' in map_data[nx][ny] and not visited[nx][ny][d]:  # 포탄이 충분하면서 다음 탐색위치가 전차이고 방문하지 않았다면
                visited[nx][ny][d]=True  # 방문 표시 후
                q.append((nx, ny, d, path+[(direction[d], 'F S') ,(direction[(d+1)%4], 'A')]))  #방향과 공격, 이동명령 경로에 추가하고 큐 넣기
        
        nd=(d-1)%4  # 시계 반대방향으로 탐색
        if not visited[x][y][nd]:  # 현재위치 방향의 왼쪽 방향 탐색하지 않았다면
            visited[x][y][nd]=True  # 방문표시 후
            q.append((x, y, nd, path))  # 큐 넣기
        
        nd=(d+1)%4  # 시계 방향으로 탐색
        if not visited[x][y][nd]:  # 현재위치 방향의 오른쪽 방향 탐색하지 않았다면
            visited[x][y][nd]=True  # 방문표시 후 
            q.append((x, y, nd, path))  # 큐 넣기
    return []  # 경로 못찾으면 빈 경로 반환


# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 자기 차례가 되어 받은 게임정보를 파싱
    print(f'----입력데이터----\n{game_data}\n----------------')
    parse_data(game_data)

    # 파싱한 데이터를 화면에 출력하여 확인
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(allies)})')
    for k, v in allies.items():
        if k == 'A':
            print(f'A (내 전차) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 대전차 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 전차) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(allies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'H (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 전차) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])


    N=len(map_data)
    
    for i in range(N):  # 맵 전체 완전탐색
        for j in range(N):
            if map_data[i][j] in ('G','W','R'):continue  # 일반 지형지물이면 패스
            if map_data[i][j] == 'A': my_position = [i,j]  # 내 위치 찾고 저장
            elif map_data[i][j] == 'X': target_position = [i,j]  # 적 포탑위치 찾고 저장
    
    # 적 포탑 하나만 있거나 적 전차는 존재하나 보급창이 존재하지 않을 경우
    # 모두 장애물 취급하고 적 포탑을 목표로 경로 찾기
    path=bfs(my_position, target_position)  
    
    if path:  # 경로가 존재하면 
        dirct, cmnd=path[0]  # 경로의 첫번째 요소 뽑아서
        output=f'{dirct} {cmnd}'  # 명령 생성
    
    if not output:output='S'  # 명령이 나오지 않을 경우 stay
    
    game_data = submit(output)  # 명령 전송
    print(output)

# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()