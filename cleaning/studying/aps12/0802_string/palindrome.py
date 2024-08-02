def find(matrix):
    for i in range(N):
        for j in range(N-M+1):
            conf = matrix[i][j:j+M]
            conf_p = conf[::-1]
            if conf == conf_p:
                return conf
            # for k in range(M//2):
            #     if conf[k] != conf[M-1-k]:
            #         break
            #     else:
            #         continue
            # return conf
    return False


def transpose(matrix):
    for i in range(N):
        for j in range(N):
            if i < j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    mat = [[s for s in input()] for _ in range(N)]

    result = find(mat)
    if find(mat) is False:
        new_mat = transpose(mat)
        result = find(new_mat)
    print(f'#{tc+1}', ''.join(result))
    # print(mat)


    # for i in range(N):
    #     for j in range(N-M+1):
    #         find_pal(mat[i][j:j+M])

