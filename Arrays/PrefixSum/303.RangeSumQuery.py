class Prefix:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def rangeSum(self, right, left):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)
        

