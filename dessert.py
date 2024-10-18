"""
한 바퀴를 만들 수 있느냐?
1. 출발점 위치 고려
2. 간만큼 돌아올 수 있어야됨.
    1. 1번 방향으로 뻗으면서 갈 수 있는 점 체크
    2. 체크하면서 count_1
    3. 2번 방향으로 뻗으면서 갈 수 있는 점 체크
    4. 체크하면서 count_2
    5. 갔던 카운트만큼 3, 4 진행하되, 끝점이 매트릭스 안인지 체크
    6. 지나간 점 중복여부 체크
"""
def finder():
    ans = -1
    for i in range(1, N-1):
        for j in range(N-2):
            stt = (i, j)
            res = calculator(stt)
            ans = max(ans, res)
    return ans


def calculator(pit):
    res = -1
    dir = {'1': (1, 1), '2': (1, -1), '3': (-1, -1), '4': (-1, 1)}
    count_1, count_2 = 0, 0
    x, y = pit[0], pit[1]
    pos_list1 = [mat[x][y]]    
    while True:
        pass


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    
    ans = finder()
    print(f'#{tc+1} {ans}')