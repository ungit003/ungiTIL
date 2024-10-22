from libs._bridge import init, submit, close
from collections import deque

NICKNAME = '탱크1'
game_data = init(NICKNAME)


# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
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

my_pos = tuple()
for i in range(len(map_data)):
    for j in range(len(map_data[i])):  # 2차원 배열의 경우 두 번째 len을 사용
        if map_data[i][j] == 'A':
            my_pos = (i, j)
if my_pos == (1, 15):
    cnt = 0
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
                print(f'A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 대전차 포탄: {v[3]}개')
            elif k == 'H':
                print(f'H (아군 포탑) - 체력: {v[0]}')
            else:
                print(f'{k} (아군 탱크) - 체력: {v[0]}')

        print(f'\n[적군 정보] (적군 수: {len(allies)})')
        for k, v in enemies.items():
            if k == 'X':
                print(f'H (적군 포탑) - 체력: {v[0]}')
            else:
                print(f'{k} (적군 탱크) - 체력: {v[0]}')

        print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
        for i in range(len(codes)):
            print(codes[i])


        # 탱크의 동작을 결정하기 위한 알고리즘을 구현하고 원하는 커맨드를 output 변수에 담기
        # 코드 구현 예시: '아래쪽으로 전진'하되, 아래쪽이 지나갈 수 있는 길이 아니라면 '오른쪽로 전진'하라

        # 1번 탱크
        if cnt == 0:
            output = 'L A'
        elif cnt == 1:
            output = 'U A'
        else:
            output = None  # output을 None으로 초기화
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상
            d_dict = {(0, 1): 'R F S', (1, 0): 'D F S', (0, -1): 'L F S', (-1, 0): 'U F S'}

            for i in range(len(map_data)):
                for j in range(len(map_data[i])):  # 2차원 배열의 경우 두 번째 len을 사용
                    if map_data[i][j] == 'A':
                        my_pos = (i, j)

            for elem in d:
                dx, dy = elem[0] + my_pos[0], elem[1] + my_pos[1]
                if 0 <= dx < len(map_data) and 0 <= dy < len(map_data[0]):  # 두 번째 조건 수정
                    if map_data[dx][dy] in ['E1', 'E2', 'E3']:
                        output = d_dict[elem]
                        break  # 유효한 output이 설정되면 루프 종료

            if output is None:  # 어떤 방향으로도 이동할 수 없다면 기본값 설정
                output = 'L F S'

        game_data = submit(output)
        cnt += 1

    # 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
    close()

else:
    # 방향 계산하는 함수
    def get_direction(start,end):
        new_direction=[end[0]-start[0],end[1]-start[1]]
        if new_direction == [0,1]:
            return 'R'
        elif new_direction == [0,-1]:
            return 'L'
        elif new_direction == [1,0]:
            return 'D'
        elif new_direction == [-1,0]:
            return 'U'
        else:
            return 'S'

    # 적 포탑까지의 최소 거리를 구하는 함수
    def find_min_turns_to_tower(start):
        dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 방향 이동 벡터 (우, 하, 좌, 상)
        N = len(map_data)  # 맵의 세로 크기
        M = len(map_data[0])  # 맵의 가로 크기
        q = deque()
        
        # 방문 배열 (각 좌표에서 최소 턴 기록)
        visited = [[float('inf') for _ in range(M)] for _ in range(N)]
        visited[start[0]][start[1]] = 0  # 시작 위치는 턴 0으로 방문
        
        q.append((start[0], start[1], 0, []))  # x, y, 현재 소모 턴, 경로 리스트
        min_turns=10000
        min_turns_route=[]
        while q:
            x, y, turns, path = q.popleft()

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 맵 범위를 벗어나면 패스
                    continue

                new_tile = map_data[nx][ny]

                # 풀이거나 탱크일 경우 (이동하는 데 1턴 소모)
                if new_tile == 'G' or new_tile.startswith('E'):  # 풀 또는 적 탱크일 때
                    if visited[nx][ny] > turns + 1:  # 최소 턴으로 방문하지 않은 곳이면
                        visited[nx][ny] = turns + 1
                        q.append((nx, ny, turns + 1, path + [[nx, ny]]))  # 1턴 추가하고 이동

                # 나무를 만나면 (부수기 + 이동, 2턴 소모)
                elif new_tile == 'T':
                    if visited[nx][ny] > turns + 2:  # 최소 턴으로 나무를 파괴하지 않은 곳이면
                        visited[nx][ny] = turns + 2
                        q.append((nx, ny, turns + 2, path + [[nx, ny]]))  # 2턴 추가하고 이동

                # 적 포탑을 만나면 종료
                elif new_tile == 'X':
                    if turns < min_turns:
                        min_turns=turns
                        min_turns_route = path +[[nx,ny]]    
        return min_turns, min_turns_route


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
                print(f'A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 대전차 포탄: {v[3]}개')
            elif k == 'H':
                print(f'H (아군 포탑) - 체력: {v[0]}')
            else:
                print(f'{k} (아군 탱크) - 체력: {v[0]}')

        print(f'\n[적군 정보] (적군 수: {len(allies)})')
        for k, v in enemies.items():
            if k == 'X':
                print(f'H (적군 포탑) - 체력: {v[0]}')
            else:
                print(f'{k} (적군 탱크) - 체력: {v[0]}')

        print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
        for i in range(len(codes)):
            print(codes[i])

        output = 'S'  # 알고리즘 결괏값이 없을 경우를 대비하여 초기값을 S로 설정

        # 유닛들 위치 파악하기
        my_position = {}
        my_H=[-1,-1]
        en_position = {}
        en_X =[-1,-1]
        for i in range(len(map_data)):
            for j in range(len(map_data[0])):
                if map_data[i][j].startswith('A'):
                    my_position[map_data[i][j]]=[i,j]
                elif map_data[i][j] == 'H': # 내포탑 발견시
                    my_H[0]=i
                    my_H[1]=j
                elif map_data[i][j].startswith('E'):
                    en_position[map_data[i][j]]=[i,j]
                elif map_data[i][j]== 'X':
                    en_X[0]=i
                    en_X[1]=j
        print(my_position)
        # 포탑까지의 최소 경로 구하기
        min_turns,route = find_min_turns_to_tower(my_position['A'])
        
        # 적 탱크가 포탑으로 가는 길에 있을 때만 공격하고 아니면 지나쳐서 포탑으로 가는 함수
        if len(route) >0:
            for next_position in route:
                new_tile=map_data[next_position[0]][next_position[1]]
                direction=get_direction(my_position['A'], next_position)
                if new_tile =='T': # 나무를 만난다면
                    output = f'{direction} F M' # 일반 포탄 발사
                    break
                elif new_tile.startswith('E'): # 적탱크를 만난다면
                    output = f'{direction} F S' # 대전차 포탄 발사
                    break
                elif new_tile=='X': # 적포탑이라면
                    output = f'{direction} F M' # 일반 포탄 발사
                    break
                elif new_tile=='G': # 풀이라면
                    output = f'{direction} A' 
                    break
                else:
                    output ='S'
                    break
                

        # while 문의 끝에는 다음 코드가 필수로 존재하여야 함
        # output에 담긴 값은 submit 함수를 통해 배틀싸피 메인 프로그램에 전달
        game_data = submit(output)
        
        # 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
        close()