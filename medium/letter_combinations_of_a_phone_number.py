class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        combos = [""]

        for digit in digits:
            new_combos = []
            for letter in mapping[digit]:
                for combo in combos:
                    new_combos.append(combo + letter)

            combos = new_combos
        
        return combos