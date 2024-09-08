"""
문제 요약
N * N 게임판
정사각형 블록, 삼각형 블록 * 4, 웜홀, 블랙홀
블록 평면에 부딪히면 정반대, 경사면에 부딪히면 꺾임
웜홀에 들어가면 해당 번호의 다른 웜홀로 나옴
블랙홀에 들어가거나 자기 위치로 되돌아오면 END
벽, 블록에 부딪히면 점수 + 1
아무 장애물이 없는 곳에서만 출발 가능
점수 최댓값?
"""
'''
풀이 전략
1. 입력 받기

2. 코드 만들기
2-1. 출발하는 지점
2-2. 지점마다 네개의 방향
2-3. 튕기기 계산
2-4. 점수 비교
'''


def sp(m):
    arr = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == 0:
                arr.append((i, j))
    return arr


def game(stt, drt):
    cnt = 0
    i, j = stt

    def direction_change(num, drt):  # 블록 1 ~ 5, 1은 벽과 같음
        print('어디 갖다 박았니?', num)
        if num == 5:
            print('wall')
            new_drt = (drt + 2) % 4

        else:
            if num % 4 == drt:
                print('좌회전')
                new_drt = (drt - 1) % 4

            elif (num + 1) % 4 == drt:
                print('우회전')
                new_drt = (drt + 1) % 4

            else:
                print('wall2')
                new_drt = (drt + 2) % 4

        # new_i, new_j = i + d[new_drt][0], j + d[new_drt][1]
        return new_drt

    def jump(x, y):
        stt_warm = mat[x][y]
        for nx in range(N):
            for ny in range(N):
                if mat[nx][ny] == stt_warm and (nx, ny) != (x, y):
                    return nx, ny
        return None, None

    stopper = 0
    while True:
        if stopper == 5:
            print('스토퍼')
            break
        i, j = i + d[drt][0], j + d[drt][1]
        print(i, j, drt)

        if not (0 <= i < N) or not (0 <= j < N):
            print('out')
            drt = direction_change(5, drt)
            print(i, j, drt)
            print()
            cnt += 1
            continue

        elif mat[i][j] in [1, 2, 3, 4, 5]:
            drt = direction_change(mat[i][j], drt)
            print(i, j, drt)
            print()
            cnt += 1
        elif mat[i][j] in [6, 7, 8, 9, 10]:
            print('warm')
            i, j = jump(i, j)

        if (i, j) == stt:
            print('comeback')
            break

        if mat[i][j] == -1:
            print('black')
            break
        stopper += 1
    return cnt


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    stt_list = sp(mat)
    max_score = 0
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for elem in stt_list:
        for k in range(4):
            print('-----')
            print('start')
            print(elem, k)
            max_score = max(game(elem, k), max_score)
            print('game over', max_score)

    print(f'#{tc + 1}', max_score)
