def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
        
    return transposed


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


m_input = input("Enter number of rows (M): ")
n_input = input("Enter number of columns (N): ")

m = int(m_input)
n = int(n_input)

print(f"Enter the {m}x{n} matrix row by row:")

matrix = []
for i in range(m):
    row_input = input(f"Row {i + 1}: ")
    row = list(map(int, row_input.split()))
    matrix.append(row)

print("\nOriginal Matrix:")
print_matrix(matrix)

transposed = transpose_matrix(matrix)

print("\nTransposed Matrix:")
print_matrix(transposed)
