def ContainerWithMstWtr(height):

    res = 0

    left = 0
    right = len(height)-1

    while left < right:
        area = (right - left ) * min(height[left], height[right])
        res = max(area, res)


        if height[left] < height[right]:
            left += 1
        else:
            right -=1
    return res


if __name__ == '__main__':
    print(ContainerWithMstWtr([1,8,6,2,5,4,8,3,7]))
    