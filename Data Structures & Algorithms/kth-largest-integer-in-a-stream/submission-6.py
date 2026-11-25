class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
        

    def add(self, val: int) -> int:
        i = 0
        for value in self.nums:
            if value > val:
                break
            i += 1
        print(self.nums)
        self.nums = self.nums[:i] + [val] + self.nums[i:]
        print(self.nums)
        return self.nums[len(self.nums) - self.k]
