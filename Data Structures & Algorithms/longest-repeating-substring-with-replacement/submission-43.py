class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        mx = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            mx = max(mx, count[s[right]])
            if (right - left + 1) - mx > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
        
        