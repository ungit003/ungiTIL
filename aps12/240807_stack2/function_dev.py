ans = []


def solution(progresses, speeds):
    global ans
    N = len(progresses)
    print(N)
    while progresses[0] < 100:
        for i in range(N):
            progresses[i] += speeds[i]
    print(progresses)

    for i in range(N):
        if progresses[i] < 100:
            count = i
            break
        if progresses[-1] > 100:
            count = N

    new_prog = progresses[count:]
    new_spee = speeds[count:]
    ans.append(count)

    print(new_prog)
    print(new_spee)
    print(ans)

    if len(new_prog) > 0:
        return solution(new_prog, new_spee)
    else:
        return ans


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))

# count = 0
# for i in range(N):
#     count += 1
#     if progresses[i] < 100:
#         break
# if count == 1:
#     ans.append(count)
#     return ans