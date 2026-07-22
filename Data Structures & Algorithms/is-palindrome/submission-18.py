class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        first = 0
        last = l - 1
        for _ in range(0,l):
            print(first)
            while (not s[first].isalnum()) and first < last:
                first += 1
            print(first)
            while (not s[last].isalnum()) and last > first:
                last -= 1
            if s[first].upper() != s[last].upper():
                return False
            first += 1
            last -= 1
            if first > last:
                return True
        return True
        