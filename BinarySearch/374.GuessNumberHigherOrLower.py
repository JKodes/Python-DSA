def guessNumber() -> int:
    left = 1
    right = n
        
    while left < right:
        mid = (left + right) // 2
        res = guess(mid)
            
        if res > 0:
            left = mid + 1
        elif res < 0:
            right = mid - 1
        else:
            return mid


if __name__ == '__main__':
    print()