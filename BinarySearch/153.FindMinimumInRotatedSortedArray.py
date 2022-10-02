def FindMinimumInRotatedSortedArray(nums):
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left + right) //2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid 

    return nums[left]



if __name__ == '__main__':
    print(FindMinimumInRotatedSortedArray([4,5,6,7,0,1,2]))
    print(FindMinimumInRotatedSortedArray([3,4,5,1,2]))
    print(FindMinimumInRotatedSortedArray([11,13,15,17]))