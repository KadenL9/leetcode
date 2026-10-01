class Solution:
    def calculate(self, s: str) -> int:
        tokens = []
        x = 0
        currnum = ''
        while x < len(s):
            if s[x] in '0123456789':
                currnum += s[x]
            elif s[x] in '+-*/':
                if len(currnum) > 0:
                    tokens.append(int(currnum))
                    currnum = ''
                tokens.append(s[x])
            else:
                if len(currnum) > 0:
                    tokens.append(int(currnum))
                    currnum = ''
            x += 1
        
        if len(currnum) > 0:
            tokens.append(int(currnum))

        # multiplication and division
        new_tokens = []
        x = 0
        while x < len(tokens):
            if tokens[x] == "*":
                new_tokens.append(new_tokens.pop(-1) * tokens[x + 1])
                x += 2
            elif tokens[x] == "/":
                new_tokens.append(new_tokens.pop(-1) // tokens[x + 1])
                x += 2
            else:
                new_tokens.append(tokens[x])
                x += 1
        
        print(new_tokens)
        total = new_tokens[0]
        x = 1
        while x < len(new_tokens):
            if new_tokens[x] == "+":
                total += new_tokens[x + 1]
                x += 2
            elif new_tokens[x] == "-":
                total -= new_tokens[x + 1]
                x += 2
            else:
                x += 1
            
        return total
