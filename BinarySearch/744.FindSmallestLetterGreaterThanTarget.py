def FindSmallestLetterGreaterThanTarget(letters):
    left = 0
    right = len(letters)


    while left < right:
        mid = (left + right) // 2

        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

