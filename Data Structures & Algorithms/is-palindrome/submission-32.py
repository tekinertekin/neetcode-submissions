class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x.upper() if x.isalnum() else "" for x in s])
        length = len(s)
        half_length = length//2
        return s[:half_length] == s[length:length-half_length-1:-1]
        