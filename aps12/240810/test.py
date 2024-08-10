numbers = [1, 1]

n = len(numbers)
subset_cnt = 2 ** n

subsets = []
for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(numbers[j])
        else:
            subset.append(-numbers[j])
    subsets.append(subset)

print(subsets)