
class Solution:
    def isValidSudoku(self, board) -> bool:
        self.b = board
        for i in range(9):
            for j in range(9):
                if self.b[i][j] != '.':
                    if self.row(i, j): return False
                    if self.col(i, j): return False
                    if self.box(i, j): return False
        return True
        
    def row(self, i, j):
        for r in range(j+1, 9):
            if self.b[i][j] == self.b[i][r]: return True
        return False

    def col(self, i, j):
        for c in range(i+1, 9):
            if self.b[i][j] == self.b[c][j]: return True
        return False

    def box(self, i, j):
        sr, sc = int(i / 3) * 3, int(j / 3) * 3
        for r in range(sr, sr+3):
            for c in range(sc, sc+3):
                if (r != i and c != j) and (self.b[r][c] == self.b[i][j]): 
                    return True
        return False
sudoku_table = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
s=Solution()
print(s.isValidSudoku(sudoku_table))