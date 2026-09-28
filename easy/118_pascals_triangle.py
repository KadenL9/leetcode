class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        rows = []
        for x in range(1, numRows + 1):
            newRow = []
            for y in range(x):
                if y == 0 or y == x - 1:
                    newRow.append(1)
                else:
                    newRow.append(rows[x - 2][y - 1] + rows[x - 2][y])
            rows.append(newRow)
        
        return rows
