# Moves of the knight in chess

col, row = input().strip()
matrix = []
a = 0
x = 0
y = 0
    
arr = ['a','b','c','d','e','f','g','h']
for i in range(8):
    if col == arr[i]:
        a = i

for i in range(8):
    matrix.append([])
    for j in range(8):
        matrix[i].append('.')
        
row = int(row)
matrix[row - 1][a] = 'N'
matrix.reverse()

for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'N':
            y = i
            x = j

for i in range(8):
    for j in range(8):
        inx = (x - j) * (y - i)
        if inx == 2 or inx == -2:
            matrix[i][j] = '*'

for roe in matrix:
    for j in roe:
        print(j, end = ' ')
    print() 
