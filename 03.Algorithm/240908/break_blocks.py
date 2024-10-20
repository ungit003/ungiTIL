"""
풀이 전략
1. 벽돌을 깨는 함수를 만든다 몇번째 행인지 만 입력받으면 될듯.?
1-1. 시계방향으로 90도 돌림
1-2. 맨 끝값 pop
1-3. 값의 크기에 따라서 폭발시킴. -> pop할 때 좌표 가져오고. 상하좌우 델타로 크기만큼 돌림.
1-3-1. 폭발 시킨애도 값이 있으면 다 폭발시킴
1-4. 폭발시킨 갯수 카운트

2. dfs 작성
몇번째 줄에서 폭발하는지 따라 입력을 새로 받아야 하니까 매트릭스를 저장해 둘 필요가 있음.
또는 매번 새로 불러와야 함.
"""
from collections import deque


def make_new():
    new_m = [[0] * H for _ in range(W)]
    for i in range(H):
        for j in range(W):
            new_m[j][H - 1 - i] = mat[i][j]
    return new_m


def breaking(s):
    cnt = 0
    cnt_zero = 0
    if len(set(stage[s])) == 1 and 0 in stage[s]:
        return cnt

    def break_more():
        bomb_size = stage[s][len(s) - 1 - cnt]
        dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        bomb_list = deque()
        for k in range(3):
            for size in range(1, bomb_size):
                dx, dy = s + dr[k][0] * size, (len(s) - 1 - cnt) + dr[k][1] * size
                if not (0 <= dx < H and 0 <= dy < W):
                    continue
                bomb_list.append((dx, dy))
        while bomb_list:
            bomb_idx = bomb_list.popleft()
            if stage[bomb_idx[0][bomb_idx[1]]] == 1:
                stage[bomb_idx[0]][bomb_idx[1]] = 0
                cnt += 1
            else:

    bomb_plus = False
    while True:
        if len(stage[s]) == 0:
            break
        bomb = stage[s].pop()
        if bomb == 0:
            cnt_zero += 1
            continue
        elif bomb == 1:
            cnt += 1
            break
        else:
            bomb_plus = True
            cnt += 1
            break

    if not bomb_plus:
        stage[s] += [0] * (cnt + cnt_zero)
        return cnt
    else:
        stage[s] += [0] * (cnt + cnt_zero)
        break_more()
        return cnt


T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(H)]

    remains = 0
    for i in range(H):
        for j in range(W):
            if mat[i][j] != 0:
                remains += 1
    print(remains)

    stage = make_new()
    for row in stage:
        print(row)
    print()
    x = breaking(0)
    for row in stage:
        print(row)
    print(x)

    # for row in mat:
    #     print(row)
    #
    # new_m = [[0] * H for _ in range(W)]
    # # for row in new_m:
    # #     print(row)
    # # print()
    # for i in range(W):
    #     for j in range(H):
    #         new_m[i][j] = mat[W - 1 - j][i]
    #         # for row in new_m:
    #         #     print(row)
    #         # print()
    #
    # for row in new_m:
    #     print(row)
