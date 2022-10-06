

def DoubleBinarySearch(nums, target, left_most):
    left = 0
    right = len(nums)-1
    i = -1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid -1
        elif nums[mid] < target:
            left = mid + 1
        else:
            i = mid
            if left_most:
                right = mid - 1
            else:
                left = mid + 1
    return i
    


if __name__ == '__main__':
    left = DoubleBinarySearch([5,7,7,8,8,10], 8, True)
    right = DoubleBinarySearch([5,7,7,8,8,10], 8, False)
    print('Example 1:')
    print(left, right)
    left = DoubleBinarySearch([5,7,7,8,8,10], 6, True)
    right = DoubleBinarySearch([5,7,7,8,8,10], 6, False)
    print('Example 2:')
    print(left, right)