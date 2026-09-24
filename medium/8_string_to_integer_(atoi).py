class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        l = len(s)
        # ignore whitespace
        while index < l and s[index] == " ":
            index += 1
        
        neg = False
        if index < l:
            if s[index] == "-":
                neg = True
                index += 1
            elif s[index] == "+":
                index += 1

        num = 0
        while index < l and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1
        
        if neg:
            num *= -1

        if neg:
            num = max(-2**31, num)
        else:
            num = min(num, 2**31 - 1)
        return num