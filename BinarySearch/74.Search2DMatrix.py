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
    row = (top_row + bottom_row) // 2
    left = 0
    right = COLS - 1

    while left <= right:
        mid = (left + right) // 2

        if target > matrix[row][mid]:
            left = mid + 1
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            return True
    return False














if __name__ == '__main__':
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))


