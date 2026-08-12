class Solution:
    def intToRoman(self, num: int) -> str:
        val_pair = [(1000, "M"),
                    (900, "CM"),
                    (500, "D"),
                    (400, "CD"),
                    (100, "C"),
                    (90, "XC"),
                    (50, "L"),
                    (40, "XL"),
                    (10, "X"),
                    (9, "IX"),
                    (5, "V"),
                    (4, "IV"),
                    (1, "I")]
        
        roman = ""
        index = 0
        while num > 0:
            val, rom = val_pair[index]
            
            if num >= val:
                roman += rom
                num -= val
            else:
                index += 1

        return roman
        
