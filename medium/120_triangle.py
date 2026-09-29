class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for x in range(1, len(triangle)):
            for y in range(len(triangle[x])):
                if y == 0:
                    triangle[x][y] += triangle[x - 1][y]
                elif y == len(triangle[x]) - 1:
                    triangle[x][y] += triangle[x - 1][y - 1]
                else:
                    triangle[x][y] += min(triangle[x - 1][y - 1], triangle[x - 1][y])
        
        return min(triangle[-1])
