class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        strs = [""]
        for x in range(n * 2):
            new_strs = []
            for s in strs:
                if s.count("(") < n:
                    new_strs.append(s + "(")
                
                if s.count(")") < s.count("("):
                    new_strs.append(s + ")")
            
            strs = new_strs
        
        return strs