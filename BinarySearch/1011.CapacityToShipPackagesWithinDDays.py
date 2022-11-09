def DaysToShip(weights, days):
    left = max(weights)
    right = sum(weights)


    while left < right:
        mid = (left + right) // 2

        if package_ships(mid, weights, days):
            right = mid
        else:
            left = mid + 1

    return right

def package_ships(candidate, weights, days):
    current_weight = 0
    days_taken = 1

    for weight in weights:
        current_weight += weight

        if current_weight > candidate:
            days_taken += 1
            current_weight = weight

    return days_taken <= days



if __name__ == '__main__':
    print(DaysToShip([1,2,3,4,5,6,7,8,9,10], 5))