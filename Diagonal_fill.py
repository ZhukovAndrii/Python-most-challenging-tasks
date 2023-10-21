# Diagonal fill of a matrix

n, m = input().split()
n, m = int(n), int(m)
sum = 1
s = 0
matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(0)

while s != m * n +1:
    for i in range(n):
        for j in range(m):
            if j + i == s:
                matrix[i][j] = sum
                sum += 1
    s += 1
    
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()
