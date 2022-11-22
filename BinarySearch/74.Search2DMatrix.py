def searchMatrix(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])


    top_row = 0
    bottom_row = ROWS - 1

    while top_row <= bottom_row:
        row = (top_row + bottom_row) // 2

        if target > matrix[row][-1]:
            top_row = row + 1
        elif target < matrix[row][0]:
            bottom_row = row - 1
        else:
            break

    if not(top_row <= bottom_row):
        return False
    














if __name__ == '__main__':
    print(searchMatrix(matrix, target))


