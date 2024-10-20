T = int(input())
for tc in range(T):
    N = int(input())
    buses = [list(map(int, input().split())) for _ in range(N)]
    stop_num = int(input())
    stops = [int(input()) for _ in range(stop_num)]

    bus_stop = [0] * 5001
    for bus in buses:
        for i in range(bus[0], bus[1] + 1):
            bus_stop[i] += 1

    print(f'#{tc+1}', *[bus_stop[i] for i in stops])
