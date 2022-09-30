def maximumSubarray(nums):
    maximum_sum = nums[0]
    current_sum = 0


    for num in nums:
        current_sum = max(current_sum, 0)
        current_sum += num
        maximum_sum = max(maximum_sum, current_sum)
    return maximum_sum









if __name__ == '__main__':
    print(maximumSubarray([-2,1,-3,4,-1,2,1,-5,4]))
    print(maximumSubarray([1]))
    print(maximumSubarray([5,4,-1,7,8]))