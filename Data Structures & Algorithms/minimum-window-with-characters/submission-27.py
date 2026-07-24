class Solution:
    def _check(self, d, chk):
        for x in chain(range(ord('a'), ord('z') + 1), range(ord('A'), ord('Z') + 1)):
            if d[x] > chk[x]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        d = {x:0 for x in chain(range(ord('a'), ord('z') + 1), range(ord('A'), ord('Z') + 1))}
        chk = {x:0 for x in chain(range(ord('a'), ord('z') + 1), range(ord('A'), ord('Z') + 1))}
        for i in range(0, len(t)):
            d[ord(t[i])] += 1
        if d[ord(s[0])]:
            chk[ord(s[0])] = 1
        l = 0
        r = 0
        mn_l, mn_r = 0 ,len(s) + 1
        while l <= r:
            cond = self._check(d, chk)
            if cond or r == len(s) - 1:
                if r - l <= mn_r - mn_l and cond:
                    mn_l, mn_r = l ,r
                if d[ord(s[l])]:
                    chk[ord(s[l])] = max(0, chk[ord(s[l])]-1)
                l += 1
            else:
                r += 1
                if d[ord(s[r])]:
                    chk[ord(s[r])] += 1
        return "" if mn_r == len(s) + 1 else s[mn_l:mn_r + 1]


        