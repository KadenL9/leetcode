class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = ["" for x in range(numRows)]
        
        step = 1
        index = 0
        for letter in s:
            rows[index] += letter
            
            if index == numRows - 1:
                step = -1
            if index == 0:
                step = 1

            index += step
        
        ans = ""
        for x in range(numRows):
            ans += rows[x]
    
        return ans
        
        