def DaysToShip(weights, days):
    left = max(weights)
    right = sum(weights)


    while left < right:
        mid = (left + right) // 2

        if self.package_ships(mid, weights, days):
            right = mid
        else:
            left = mid + 1



    