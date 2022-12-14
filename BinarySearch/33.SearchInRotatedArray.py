def SearchInRotatedArray(nums, target):
    left = 0
    right = len(nums) -1

    while (left <= right):
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid]:
                right = mid -1
            elif target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1






if __name__ == '__main__':
    print(SearchInRotatedArray([4,5,6,7,0,1,2], 0))
    print(SearchInRotatedArray([4,5,6,7,0,1,2], 3))
    print(SearchInRotatedArray([1], 0))