a = [[4,5,6,5],
     [7,2,5,1],
     [9,8,2,4]]

b = [[1,2,3],
     [5,4,3],
     [2,7,9],
     [7,6,3]]

matrix = []
for _ in range(len(a)): 
    row = [] 
    for _ in range(len(b[0])):
        row.append(0) 
    matrix.append(row) 

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            matrix[i][j] += a[i][k]*b[k][j]

print(matrix)
