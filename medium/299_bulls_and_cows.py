class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sDigits = [0] * 10
        gDigits = [0] * 10
        bulls = 0
        for x in range(len(secret)):
            s = int(secret[x])
            g = int(guess[x])
            if s == g:
                bulls += 1
            else:
                sDigits[s] += 1
                gDigits[g] += 1
        
        cows = 0
        for digit in range(10):
            digit = int(digit)
            cows += min(sDigits[digit], gDigits[digit])
    
        return f'{bulls}A{cows}B'
                