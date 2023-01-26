def sqrt(x):
    if x == 0 and x == 1:
        return x 
    
    left = 1
    right = x

    while left <= right:
        mid =(left + right) // 2

        square = mid * mid

        if square == x:
            return mid 
        elif square < x:
            left = mid + 1
            value = mid 
        else:
            right = mid - 1
    return value 

        
    '''
        [1,2,3,4,5,6,7,8,9,10,11,12,13]
               L R                   X
               M 
    '''





if __name__ == '__main__':
    print(sqrt(13))