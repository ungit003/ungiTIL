numbers = [1] * 5
target = 3


def dfs(numbers, target):
    result = 0
    n = len(numbers)

    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(numbers[j])
            else:
                subset.append(-numbers[j])
        subsets.append(subset)

    for elem in subsets:
        if sum(elem) == target:
            result += 1

    return result