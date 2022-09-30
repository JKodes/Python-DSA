def maximumSubarray(nums):
    maximum_sum = nums[0]
    current_sum = 0


    for num in nums:
        current_sum = max(current_sum, 0)
        current_sum += num
        maximum_sum = max(maximum_sum, current_sum)
    return maximum_sum









if __name__ == '__main__':
    print(maximumSubarray())