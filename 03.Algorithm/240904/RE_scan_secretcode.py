T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    mat = [[s for s in input()] for _ in range(N)]

    end = False
    while True:
        flag1 = True
        flag2 = True
        code_end = 0
        code_size = 0
        cnt = 0
        for i in range(N):
            if flag1:
                for j in range(M-1, -1, -1):
                    if mat[i][j] != '0':
                        if flag2:
                            code_end = j
                            flag2 = False
                            print(code_end)
                        code_size += 1
                        print(code_size)
                flag1 = False
            else:
                if mat[i][code_end] != '0':
                    cnt += 1
                    print(cnt)
                else:
                    break
        print(code_end, code_size, cnt)
        break




    # code = mat[cnt][code_end-14:code_end+1]
    # find = ''.join(code)
    # find2 = bin(int(find, 16))
    # print(find2)
    # find3 = ['0']
    # for i in range(2, len(find2)-2):
    #     find3.append(find2[i])
    # print(find3)
    #
    # c_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    #           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    #
    # print(len(find3))
    #
    # s_code = []
    # for i in range(8):
    #     find4 = ''.join(find3[7*i:7*(i+1)])
    #     print(find4)
    #     s_code.append(c_dict[find4])
    #
    # print(s_code)
    #
    # check = 0
    # res = 0
    # for i in range(0, 8, 2):
    #     check += s_code[i] * 3
    #     check += s_code[i+1]
    # if check % 10 == 0:
    #     res += sum(s_code)
    #
    # print(f'#{tc+1}', res)

