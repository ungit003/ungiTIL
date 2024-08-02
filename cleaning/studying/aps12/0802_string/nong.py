T = int(input())


def cal_cul(matrix):
    sum_cal = 0
    center = N // 2  # index

    center_line = matrix[center]
    sum_cal += sum(center_line)

    if N > 1:
        C = 1
        while N - C * 2 != -1:
            line1 = matrix[center + C][C:N-C]
            line2 = matrix[center - C][C:N-C]
            sum_cal += sum(line1)
            sum_cal += sum(line2)

            C += 1
    return sum_cal


for tc in range(T):
    N = int(input())
    mat = [[int(s) for s in input()] for _ in range(N)]

    result = cal_cul(mat)
    print(f'#{tc+1} {result}')




