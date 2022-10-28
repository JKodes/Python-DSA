def twosumII(nums, target):
    left = 0
    right = len(nums)-1

    while left < right:
        cur_sum = nums[left] + nums[right]

        if cur_sum > target:
            right -= 1
        elif cur_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]


if __name__ == '__main__':
    print(twosumII([2,7,11,15], 9))


