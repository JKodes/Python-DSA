def RemoveDuplicateII(nums):
    left = 2

    for right in range(2, len(nums)):
        if nums[right] != nums[left - 2]:
            nums[left] = nums[right]
            left += 1
    return left


if __name__ == '__main__':
    print(RemoveDuplicateII([0,0,1,1,1,1,2,3,3]))
    print(RemoveDuplicateII([1,1,1,2,2,3]))

