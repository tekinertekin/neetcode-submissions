class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 0:
            mult = 1
            for i in range(0, len(nums)):
                mult *= nums[i]
            return [int(mult/k) for k in nums]
        if nums.count(0) == 1:
            mult = 1
            for i in range(0, len(nums)):
                if nums[i] != 0:
                    mult *= nums[i]
            return [(mult if k == 0 else 0) for k in nums]
        if nums.count(0) > 1:
            return [0 for k in nums]
            
        