"""
암호코드 : 8자리 숫자
숫자하나 : 7bit -> 암호코드 가로길이 : 56
올바른 암호코드 : 홀수 자리 합 x 3 + 짝수자리 합 = 10의 배수
숫자를 바코드 처럼 숨겨둠

1. 입력 받기
2. 실제로 쓸 코드 부분 찾기
3. 7개씩 끊기
4. 홀수 짝수 구분하기
5. 계산해서 10의 배수인지 체크하기
6. 출력하기
"""
nums_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
             '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    barcode = [input() for _ in range(N)]
    # barcode = [x for x in [input() for _ in range(N)] if '1' in x]
    # print(barcode)

    find = None
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if barcode[i][j] == '1':
                find = barcode[i]
                break
    # print(find)

    codes = []
    for i in range(len(find)):
        codes.append(find[i])
    # print(codes)

    code = []
    while codes:
        if codes[-1] == '0':
            codes.pop()
            # print(0)
        else:
            part = ''.join(codes[-1:-8:-1][::-1])
            # print(part)
            code.append(part)
            codes = codes[:-7]
            # print(codes)
    # print(code)

    sum_c = 0
    sum_x = 0
    for i in range(len(code)):
        if i % 2 == 0:
            sum_c += nums_dict[code[i]]
            sum_x += nums_dict[code[i]]
        else:
            sum_c += nums_dict[code[i]]
            sum_x += nums_dict[code[i]] * 3
    if sum_x % 10 == 0:
        print(f'#{tc+1}', sum_c)
    else:
        print(f'#{tc+1}', 0)
