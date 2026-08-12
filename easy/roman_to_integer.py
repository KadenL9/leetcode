class Solution:
    def romanToInt(self, s: str) -> int:
        pairs = {"M": 1000,
                 "CM": 900,
                 "D": 500,
                 "CD": 400,
                 "C": 100,
                 "XC": 90,
                 "L": 50,
                 "XL": 40,
                 "X": 10,
                 "IX": 9,
                 "V": 5,
                 "IV": 4,
                 "I": 1}

        num = 0
        idx = 0
        while idx < len(s):
            if idx < len(s) - 1:
                two = s[idx:idx + 2]
                if two in pairs:
                    num += pairs[two]
                    idx += 2
                    continue
            
            num += pairs[s[idx]]
            idx += 1
        
        return num