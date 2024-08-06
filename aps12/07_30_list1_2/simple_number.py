T = int(input())

for i in range(T):
    N = int(input())
    alpha_dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    for num in alpha_dict.keys():
        while True:
            if N % num == 0:
                alpha_dict[num] += 1
                N = N // num
            else:
                break

    result = list(alpha_dict.values())
    print(f'#{i + 1}', end = ' ')
    print(*result)
