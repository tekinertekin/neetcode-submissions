import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        heapq.heapify(l)
        for point in points:
            dist = -sqrt((point[0] * point[0]) + (point[1] * point[1]))
            print(dist, l[0][1] if l else 0)
            if len(l) < k:
                heapq.heappush(l, (dist, point))
            elif dist > l[0][0]:
                heapq.heappop(l)
                heapq.heappush(l, (dist, point))

        return [x[1] for x in l]
        