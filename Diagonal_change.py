# Diagonal change

n = int(input())
matrix = [[int(num) for num in input().split()] for i in range(n)]
arr1 = []
arr2 = []
for i in range(n):
    for j in range(n):
        if i == j:
            a = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - i][j]
            matrix[n - 1 - i][j] = a
            
            
            
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()
