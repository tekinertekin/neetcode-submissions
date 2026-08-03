class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        last = 0
        while l <= r:
            mid = l + (r-l) // 2
            if sum([(x + mid - 1) // mid for x in piles]) <= h:
                last = mid
                r = mid - 1
            else:
                l = mid + 1
        return last
        