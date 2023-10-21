# Matrix multiplication

n, m = input().split()
n, m = int(n), int(m)
matrix1 = [[int(num) for num in input().split()] for i in range(n)]
a = input()
m, k = input().split()
m, k = int(m), int(k)
matrix2 = [[int(num) for num in input().split()] for i in range(m)]
matrix3 = [[0 for i in range(n)] for j in range(k)]

for i in range(n):
    for j in range(k):
        sum = 0
        for l in range(m):
            sum += matrix1[i][l] * matrix2[l][j]
        matrix3[i][j] = sum
        
for i in matrix3:
    for j in i:
        print(j, end = ' ')
    print()
