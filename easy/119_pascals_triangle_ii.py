class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        lastRow = []
        for x in range(rowIndex + 1):
            currRow = []
            for y in range(x + 1):
                if y == 0 or y == x:
                    currRow.append(1)
                else:
                    currRow.append(lastRow[y - 1] + lastRow[y])

            lastRow = currRow

        return lastRow