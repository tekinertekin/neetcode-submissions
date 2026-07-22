class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = set()
        nums.sort()
        for i in range(0, len(nums)):
            l = 0
            r = len(nums) - 1
            while l < i < r:
                if nums[l] + nums[i] + nums[r] == 0:
                    lst.add((nums[l],nums[i],nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return [list(x) for x in lst]
        