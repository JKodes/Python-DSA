def missingNumber(nums):

    n = len(nums)+ 1
    missingsum = (n/2)*(n-1)

    return missingsum - sum(nums)




if '__name__' == '__main__':
    print(missingNumber([3,0,1]))