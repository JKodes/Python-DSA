def SearchInsertPosition(nums, target):
    left = 0
    right = len(nums)-1


    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left 










if __name__ == '__main__':
    print(SearchInsertPosition([1,3,5,6], 7))