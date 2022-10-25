def containduplicates(nums):
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False

if __name__ == '__main__':
    print(containduplicates([1,2,3,1]))
    print(containduplicates([1,2,3,4]))