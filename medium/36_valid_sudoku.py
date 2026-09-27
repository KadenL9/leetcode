class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for x in range(9):
            rowseen = set()
            colseen = set()
            for y in range(9):
                rcell = board[x][y]
                ccell = board[y][x]
                if rcell != ".":
                    if rcell in rowseen:
                        return False
                    else:
                        rowseen.add(rcell)
                
                if ccell != ".":
                    if ccell in colseen:
                        return False
                    else:
                        colseen.add(ccell)

        for a in range(3):
            for b in range(3):
                boxseen = set()
                for x in range(3):
                    for y in range(3):
                        cell = board[a * 3 + x][b * 3 + y]
                        if cell != ".":
                            if cell in boxseen:
                                return False
                            else:
                                boxseen.add(cell)

        return True

