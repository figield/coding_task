def check_result(matrix, p=1):
    return check_diagonal_1(matrix, p) \
           or check_diagonal_2(matrix, p) \
           or check_rows(matrix, p) \
           or check_columns(matrix, p)


def check_diagonal_1(matrix, p):
    """
    [[1,0,0],
     [0,1,0],
     [0,0,1]]
    """
    for i in range(len(matrix)):
        if matrix[i][i] != p:
            return False
    return True


def check_diagonal_2(matrix, p):
    """
    [[0,0,1],
     [0,1,0],
     [1,0,0]]
    """
    for i in range(len(matrix)):
        if matrix[i][len(matrix) - 1 - i] != p:
            return False
    return True


def check_rows(matrix, p):
    """
    [[1,1,1],
     [0,0,0],
     [0,0,0]]
    """
    for row in matrix:
        if check_if_row_wins(row, p):
            return True
    return False


def check_if_row_wins(row, p):
    for i in row:
        if i != p:
            return False
    return True


def inverse_matrix(matrix):
    """
    [[1,0,0],
     [1,0,0],
     [1,0,0]]
      ->
    [[1,1,1],
     [0,0,0],
     [0,0,0]]
    """
    inverse = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        inverse.append(new_row)
    return inverse

# >>> matrix =  [[1,2,3], [1,2,3],[1,2,3]]
# >>> inverse_matrix(matrix)
# [[1, 1, 1], [2, 2, 2], [3, 3, 3]]


def check_columns(matrix, p):
    """
    [[1,0,0],
     [1,0,0],
     [1,0,0]]
    """
    return check_rows(inverse_matrix(matrix), p)
