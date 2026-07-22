class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for k in strs:
            l = [x for x in k]
            l.sort()
            if str(l) in d:
                d[str(l)].append(k)
            else:
                d[str(l)] = [k]
        return [y for y in d.values()]
        