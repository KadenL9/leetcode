class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0:
            if len(p) >= 2 and p[1] == "*":
                return self.isMatch(s, p[2:])
            return len(p) == 0
        
        if len(p) == 0:
            return len(s) == 0
            
        if len(p) == 1:
            if len(s) > 1:
                return False

            return p == "." or p == s

        if p[1] == "*":
            if p[0] == s[0] or p[0] == ".":
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s, p[2:])
        else:
            if p[0] == s[0] or p[0] == ".":
                return self.isMatch(s[1:], p[1:])
            else:
                return False