def solution(priorities, location):
    new_pri = []
    for i in range(len(priorities)):
        new_pri.append([i, priorities[i]])

    count = 0
    while new_pri:
        change = False
        for i in range(1, len(new_pri)):
            if new_pri[0][1] < new_pri[i][1]:
                change = True
        if change:
            new_pri.append(new_pri.pop(0))
            continue
        a = new_pri.pop(0)
        count += 1
        if a[0] == location:
            return count


print(solution([1, 1, 9, 1, 1, 1], 0))
