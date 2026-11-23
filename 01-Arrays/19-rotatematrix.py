# Rotate_matrix by 90 degree
# Brute Force Approach 
# -> Take the dummy matrix 

def rotated_matrix(matrix):
    n = len(matrix)
    rotated_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n-i-1] = matrix[i][j]
    
    # Copy the element back into the matrix
    for i in range(n):
        matrix[i] = rotated_matrix[i]
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotated_matrix(matrix))


# Optimal Solution :
# Approach :
# -> Find the transpose of the matrix (i.e row becomes column)
# -> Reverse the row elements

def rotated_matrix(matrix):
    n = len(matrix)
    # Transpose of matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
    # reversing the element of row
    for i in range(n):
        for j in range(n//2):
            matrix[i][j] , matrix[i][n-1-j] = matrix[i][n-1-j] , matrix[i][j] 
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotated_matrix(matrix))
