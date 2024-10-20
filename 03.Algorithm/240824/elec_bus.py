from collections import deque


T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))

    bus_stop = deque(range(1, N + 1))
    energy = K
    cnt = 0
    while bus_stop:
        a = bus_stop.popleft()
        energy -= 1

        if len(bus_stop) == 0 and energy >= 0:
            print(f'#{tc + 1} {cnt}')
            break

        if energy < 0:
            print(f'#{tc+1} 0')
            break

        if a in chargers:
            if a != chargers[-1]:
                n_charger = chargers.index(a) + 1
                if chargers[n_charger] - a > energy:
                    energy = K
                    cnt += 1
            else:
                if bus_stop[-1] - a > energy:
                    energy = K
                    cnt += 1

