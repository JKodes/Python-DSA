def DoubleBinarySearch(self, nums, target, left_most):
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

    



        