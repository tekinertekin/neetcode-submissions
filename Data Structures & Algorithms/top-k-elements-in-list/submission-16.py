class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        sorted_d = dict(sorted(d.items(), key=lambda d: d[1], reverse=True))
        return list(sorted_d.keys())[0:k]