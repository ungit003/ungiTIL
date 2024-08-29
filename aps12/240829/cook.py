T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    nums = list(range(N))

    subsets = []
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(nums[j])
        if len(subset) == N // 2:
            subsets.append(subset)

    points = []
    for elem1 in subsets:
        elem2 = list(range(N))
        for i in elem1:
            elem2.remove(i)
        comb1 = []
        for i in range(1 << len(elem1)):
            comb = []
            for j in range(len(elem1)):
                if i & (1 << j):
                    comb.append(elem1[j])
            if len(comb) == 2:
                comb1.append(comb)
        comb2 = []
        for i in range(1 << len(elem2)):
            comb = []
            for j in range(len(elem2)):
                if i & (1 << j):
                    comb.append(elem2[j])
            if len(comb) == 2:
                comb2.append(comb)
        point1 = 0
        for elem in comb1:
            point1 += mat[elem[0]][elem[1]]
            point1 += mat[elem[1]][elem[0]]
        point2 = 0
        for elem in comb2:
            point2 += mat[elem[0]][elem[1]]
            point2 += mat[elem[1]][elem[0]]
        points.append(abs(point1 - point2))
    print(f'#{tc + 1} {min(points)}')
