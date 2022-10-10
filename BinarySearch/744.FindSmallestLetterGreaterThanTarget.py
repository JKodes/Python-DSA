def FindSmallestLetterGreaterThanTarget(letters, target):

    if target < letters[left] or 
    left = 0
    right = len(letters)


    while left < right:
        mid = (left + right) // 2

        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return letters[left]

