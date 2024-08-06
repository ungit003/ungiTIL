# import sys
# sys.stdin = open("input_string.txt", "r")

T = 10

for _ in range(T):
    tc = int(input())
    want_find = input()
    in_here = input()

    count = 0
    for i in range(len(in_here) - len(want_find) + 1):
        if in_here[i : i + len(want_find)] == want_find:
            count += 1

    print(f'#{tc} {count}')