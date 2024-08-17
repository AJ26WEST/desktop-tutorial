# Get the dimensions and elements for the first matrix
rows_matrix1 = int(input("Enter the number of rows for Matrix 1: "))
cols_matrix1 = int(input("Enter the number of columns for Matrix 1: "))

print("Enter the elements of Matrix 1:")
matrix1 = []
for i in range(rows_matrix1):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Get the dimensions and elements for the second matrix
rows_matrix2 = int(input("Enter the number of rows for Matrix 2: "))
cols_matrix2 = int(input("Enter the number of columns for Matrix 2: "))

print("Enter the elements of Matrix 2:")
matrix2 = []
for i in range(rows_matrix2):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Check if matrix multiplication is possible
if cols_matrix1 != rows_matrix2:
    print("Matrix multiplication not possible")
else:
    # Initialize the resultant matrix with zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]
    
    # Perform matrix multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    # Print the resultant matrix
    print("Resultant Matrix:")
    for row in result:
        print(row)
