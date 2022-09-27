def PeakIndexInAMountainArray(arr):
    left = 0
    right = len(arr) -1


    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            right = mid
        else: 
            left = mid + 1

    return left


if __name__ =='__main__':
    print(PeakIndexInAMountainArray([0,1,0]))