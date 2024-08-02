# T = 10
for j in range(10) :
    N = int(input())
    # height = list(map(int, input().split()))
    # height.insert(N, 0)
    # height.insert(N+1, 0)
    # height.insert(0, 0)
    # height.insert(1, 0)
    height = [0, 0] + list(map(int, input().split())) + [0, 0]

    view = 0
    for i in range(2, N+2) :
        h_check = height[i-2:i+3]
        highest = max(h_check)
        h_check.sort()
        if highest == height[i] :
            view += height[i] - h_check[3]

    print(f'{j+1} {view}')