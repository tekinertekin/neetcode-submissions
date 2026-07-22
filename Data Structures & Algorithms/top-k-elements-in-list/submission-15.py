class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)
        sorted_d = dict(sorted(d.items(), key=lambda d: d[1], reverse=True))
        print(sorted_d)
        l = []
        for key, value in sorted_d.items():
            if len(l) >= k:
                break
            l.append(key)
        return l