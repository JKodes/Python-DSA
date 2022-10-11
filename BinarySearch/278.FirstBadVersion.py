def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2
        