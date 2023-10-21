# Whether matrix is magical or not

n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
arr = []
sum1 = 0
sum2 = 0

arr2 = []
for i in range(1, (n * n) + 1):
    arr2.append(i)

for i in range(n):
    for j in range(n):
        for k in arr2 :
            if matrix[i][j] == k:
                arr2.remove(k)
                
for i in range(n):
    arr.append(sum(matrix[i]))

for i in range(n):
    sum = 0
    for j in range(n):
        if i == j:
            sum1 += matrix[i][j]
        if i == n - 1 - j:
            sum2 += matrix[i][j]
        sum += matrix[j][i]
    arr.append(sum)
            
arr.append(sum1)
arr.append(sum2)

flag = True

for i in range(len(arr) - 1):
    if arr[i] != arr[i + 1]:
        flag = False
if flag and len(arr2) == 0:
    print('YES')
else:
    print('NO')
