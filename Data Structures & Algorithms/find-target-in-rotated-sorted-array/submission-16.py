class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            print(l,mid,r)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[mid] >= target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return l if nums[l] == target else -1 