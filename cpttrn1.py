def goup(matrix):
    for col in matrix:
        print(''.join(col))




test = int(input())
for iteration in range(0,test):
    matrix = []
    row,column = input().split()
    row=int(row)
    column=int(column)
    for i in range(0,row):
        matrix.append([])
        for c in range(0,column):
            if (c + i)%2==0:
                matrix[i].append('*')
            else:
                matrix[i].append('.')
    goup(matrix)
    print('\n')
