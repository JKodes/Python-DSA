def ContainerWithMstWtr(height):

    res = 0

    left = 0
    right = len(height)-1

    while left < right:
        area = (right - left ) * min(height[l], height[r])
        res = max(area, res)


        