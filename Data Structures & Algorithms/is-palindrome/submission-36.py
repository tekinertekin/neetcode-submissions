class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while True:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if start >= end:
                break 
            if s[start].upper() != s[end].upper():
                return False
            start += 1
            end -= 1
        return True
        s = "".join([x.upper() if x.isalnum() else "" for x in s])
        length = len(s)
        half_length = length//2
        return s[:half_length] == s[length:length-half_length-1:-1]
        