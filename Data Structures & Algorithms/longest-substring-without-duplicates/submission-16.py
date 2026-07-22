class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_dict = {x:-1 for x in s}
        mx = 0
        last_point = 0
        for i in range(0,len(s)):
            if s_dict[s[i]] != -1 and last_point < s_dict[s[i]] + 1:
                last_point = s_dict[s[i]] + 1
            s_dict[s[i]] = i
            if (i - last_point) + 1 > mx:
                mx = (i - last_point) + 1
        return mx
        