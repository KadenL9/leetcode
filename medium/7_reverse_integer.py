class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        if neg:
            x *= -1
        
        ans = int(str(x)[::-1])

        if neg:
            ans *= -1
        
        if ans > 2**31 - 1 or ans < -1 * (2**31):
            return 0
        return ans