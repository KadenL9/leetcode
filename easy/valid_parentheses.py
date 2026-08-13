class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ["(", "[", "{"]:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False

                if (bracket == "}" and stack.pop() != "{") or \
                   (bracket == "]" and stack.pop() != "[") or \
                   (bracket == ")" and stack.pop() != "("):
                   return False
        
        return len(stack) == 0