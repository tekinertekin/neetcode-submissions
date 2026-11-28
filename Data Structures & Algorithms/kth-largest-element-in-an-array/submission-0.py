import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = []
        for num in nums:
            if len(l) < k:
                heapq.heappush(l, num)
            elif l[0] < num:
                heapq.heapreplace(l, num)
        return l[0]
        