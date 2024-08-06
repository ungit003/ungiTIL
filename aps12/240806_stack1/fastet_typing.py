T = int(input())
for tc in range(T):
    long, short = input().split()

    a = long.replace(short, ' ')
    print(f'#{tc+1} {len(a)}')