class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        for x in range(n - 1):
            newnum = ""
            idx = 1
            count = 1
            last = num[0]
            while idx < len(num):
                if num[idx] == last:
                    count += 1
                else:
                    newnum += str(count) + last
                    count = 1
                    last = num[idx]

                idx += 1
            
            newnum += str(count) + last
            num = newnum
        
        return num
