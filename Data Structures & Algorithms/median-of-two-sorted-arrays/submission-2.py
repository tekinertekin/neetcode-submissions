class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_left = (len(nums1) + len(nums2)) // 2
        if len(nums1) >= len(nums2):
            small = nums2
            big = nums1
        else:
            small = nums1
            big = nums2
        small = [float('-inf')] + small + [float('inf')]
        big = [float('-inf')] + big + [float('inf')]
        l = 0
        r = len(small) - 2
        while True:
            i = l + (r - l) // 2
            j = total_left - i
            if small[i] <= big[j+1] and big[j] <= small[i+1]:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(big[j+1], small[i+1])
                else:
                    return (max(small[i], big[j]) + min(big[j+1], small[i+1])) / 2
            if small[i] > big[j+1]:
                r = i - 1
            else:
                l = i + 1