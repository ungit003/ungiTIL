T = int(input())
for tc in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    sets = set(range(1, 10))
    count = 1
    for raw in sudoku:
        if set(raw) != sets:
            count = 0

        else:
            # col = list(zip(*sudoku))
            # for i in range(9):
            for col in zip(*sudoku):
                if set(col) != sets:
                    count = 0

                else:
                    for i in range(0, 9, 3):
                        for j in range(0, 9, 3):
                            thr_by_thr = set()
                            for ii in range(3):
                                for jj in range(3):
                                    thr_by_thr.add(sudoku[i+ii][j+jj])
                            if thr_by_thr != sets:
                                count = 0
                                break

    print(f'#{tc+1}', count)