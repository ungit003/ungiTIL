def solution(progresses, speeds):
    ans = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            # print(progresses, speeds)

        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            # print(progresses, speeds, cnt)

        if cnt > 0:
            ans.append(cnt)
            # print(ans)

    return ans

# def solution(progresses, speeds):
#     ans = []
#     N = len(progresses)
#     print(N)
#
#     count = 0
#
#     while progresses[0] < 100:
#         for i in range(N):
#             progresses[i] += speeds[i]
#
#             if progresses[0] >= 100:
#                 progresses.pop(0)
#                 speeds.pop(0)
#                 count += 1
#                 N -= 1
#
#             if count > 0:
#                 ans.append(count)
#
#     return ans

    # count = 0
    # for i in range(N):
    #     if progresses[i] < 100:
    #         count = i
    #     if progresses[-1] >= 100:
    #         count = i
    #
    # ans.append(count)
    # new_prog = progresses[count:]
    # new_spee = speeds[count:]
    # print(new_prog)
    # print(new_spee)
    #
    # print(ans)
    #
    # if len(new_prog) > 0:
    #     print(len(new_prog))
    #     return solution(new_prog, new_spee)
    # else:
    #     return ans


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