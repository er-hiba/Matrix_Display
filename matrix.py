def create_matrix():
    while True :
        N = int(input("Enter number of rows: "))
        if N > 0 and N <= 10 :
            break

    while True :
        P = int(input("Enter number of columns: "))
        if P > 0 and P <= 10 :
            break

    matrix = [[0 for _ in range(P)] for _ in range(N)]
    x = 1
    for i in range(N):
        for j in range(P):
            matrix[i][j] = x
            x += 1

    return matrix

# Display the matrix
matrix = create_matrix()
print("\nOriginal matrix:")
for row in matrix:
    print(row)

# Display the matrix alternatively from left to right and right to left
print("\nThe matrix alternatively from left to right and right to left :")
for i in range(len(matrix)):
    if i % 2 == 0 :   # If the row number is even, display the row from left to right
        print(matrix[i])
        
    else:   # If the row number is odd, display the row from right to left
        print(matrix[i][::-1])
