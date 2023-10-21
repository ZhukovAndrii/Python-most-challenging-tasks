arr = list(input().split())
matrix = [[]]

for i in range(len(arr)):
    for j in range(len(arr)):
        temp = []
        temp = arr[j:j+i+1]
        if len(temp) == i + 1:
            matrix.append(temp)

print(matrix)
