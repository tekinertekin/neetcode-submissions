class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = list(set(nums))
        set_nums.sort()
        print(set_nums)
        if not set_nums:
            return 0
        l = [1]
        for i in range(1, len(set_nums)):
            l.append(l[i-1] + 1 if set_nums[i]-set_nums[i-1] == 1 else 1)
        print(l)
        return max(l)
        