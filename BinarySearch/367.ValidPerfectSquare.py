def validperfectsquare(num):
    left = 1
    right = num

    while left <= right:
        mid = (left + right) // 2

        if num == mid * mid:
            return True
        elif num < mid * mid:
            right = mid - 1
        else:
            left = mid + 1
    return False

if __name__ == '__main__':
    print(validperfectsquare(8))