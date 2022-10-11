def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2
        bad = isBadVersion(mid)
        if bad:
            right = mid
        else:
            left = mid + 1
    return left