n = int(input())
my_list = [[1], [1, 1]]

if n > 1:
    for i in range(2, n + 1):
        my_list.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                my_list[i].append(1)
            else:    
                my_list[i].append(my_list[i-1][j-1] + my_list[i-1][j])
        
print(my_list[n]) 
