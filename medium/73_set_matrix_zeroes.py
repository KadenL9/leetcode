class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        check = [False] * (m + n)

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    check[x] = True
                    check[m + y] = True
        
        for x in range(m):
            for y in range(n):
                if check[x] == True or check[m + y] == True:
                    matrix[x][y] = 0