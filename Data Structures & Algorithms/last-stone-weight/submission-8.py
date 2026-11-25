import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            last_1 = heapq.heappop(stones)
            last_2 = heapq.heappop(stones)
            if last_1 != last_2:
                if last_1 > last_2:
                    heapq.heappush(stones, last_2 - last_1)
                else:
                    heapq.heappush(stones, last_1 - last_2)
        return -stones[0] if stones else 0
        