class Solution:
    def longestPalindrome(self, s: str) -> str:
        for x in range(1, len(s)):
            for y in range(x):
                sub = s[y: len(s) - x + y + 1]
                if sub == sub[::-1]:
                    return sub
        
        return s[0]
