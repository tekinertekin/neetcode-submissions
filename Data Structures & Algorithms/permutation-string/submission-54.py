class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d = {x:0 for x in range(ord('a'), ord('z') + 1)}
        chk = {x:0 for x in range(ord('a'), ord('z') + 1)}
        for i in range(0, len(s1)):
            d[ord(s1[i])] += 1
            chk[ord(s2[i])] += 1
        if d == chk:
            return True
        for i in range(len(s1),len(s2)):
            chk[ord(s2[i])] += 1
            chk[ord(s2[i - len(s1)])] -= 1
            if d ==chk:
                return True
        return False


        