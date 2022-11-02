class Prefix:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    
        

