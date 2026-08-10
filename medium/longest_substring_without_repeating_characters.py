class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        substr = ""
        length = 0
        while right < len(s):
            if s[right] not in substr:
                substr += s[right]
                right += 1
                length = max(length, right - left)
            else:
                left += 1
                substr = substr[1:]
        
        return length
