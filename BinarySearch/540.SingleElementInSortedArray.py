def singleNonDuplicate(nums):
    left = 0
    right = len(nums)-1

    while left < right:
        mid = 2* ((left + right)// 4)

        if nums[mid] == nums[mid +1]:
            left = mid + 2
        else:
            right = mid 
    
    return nums[left]



if __name__ == '__main__':
    print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))