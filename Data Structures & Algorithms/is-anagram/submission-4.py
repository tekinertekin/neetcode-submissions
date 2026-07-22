class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [x for x in s]
        t_list = [x for x in t]
        s_list.sort()
        t_list.sort()
        return s_list == t_list
        