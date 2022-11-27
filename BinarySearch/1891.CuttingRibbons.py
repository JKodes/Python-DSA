def CuttingRibbons(ribbons, k):
    left = 1
    right = max(ribbons)


    while left <= right:
        mid = (left + right)// 2

        if can_cut(ribbons, k, mid):
            left = mid + 1
        else:
            right = mid - 1







