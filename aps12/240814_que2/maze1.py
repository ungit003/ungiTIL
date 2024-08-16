from collections import deque

T = 10
size = 16
for _ in range(T):
    tc = int(input())
    maze = [list(map(int, input().split())) for _ in range(size)]
    check = []

    for i in range(size):
        for j in range(size):
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                end = [i, j]


def bfs(s, e):
    if s == e:
        return
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    que = deque()
    for elem in d:
        a = maze[start[0]+elem[0]][start[1]+elem[1]]
        if a == 0:
            que.append(a)



