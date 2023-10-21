#Sample output

# 1 2 3
# 2 3 1
# 3 1 2
# 1 2 3
# 2 3 1
# 3 1 2
# 1 2 3

n, m = [int(num) for num in input().split()]
matrix = [num for num in range(1, m + 1)]
for i in range(n):
    for j in range(m):
        print(matrix[j], end=' ')
    pop = matrix.pop(0)
    matrix.append(pop)
    print()
