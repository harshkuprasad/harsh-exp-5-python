Rows = int(input("Give the no. of rows: "))
Columns = int(input("Give the no. of columns: "))

matrix = [[int(input()) for c in range(Columns)] for r in range(Rows)]

print("Original matrix:")
for i in range(0, Rows):
    for j in range(0, Columns):
        print(matrix[i][j], "\t", end=" ")
    print()

print("Matrix after transpose:")
for i in range(0, Columns):
    for j in range(0, Rows):
        print(matrix[j][i], "\t", end=" ")
    print()
