d = { 'UR': (-1, 1), 'DR': (1, 1), 'UL': (-1, -1), 'DL': (1, -1)}
x = y = 0 
N = 3
for elem in d:
    i = 1
    
    
    while True:
        dx, dy = x + d[elem][0] * i, y + d[elem][1] * i
        pit = dx * N + dy
        print(dx, dy, pit)
        if not (0 <= dx < N) or not (0 <= dy < N):
            break
        if pit >= N * N:
            break

        i += 1 
