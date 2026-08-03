class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r - 1:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        return -1
        