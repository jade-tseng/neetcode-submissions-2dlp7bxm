class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(9):
            rows = set()
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                elif val in rows:
                    return False
                else:
                    rows.add(val)
        
        for r in range(9):
            cols = set()
            for c in range(9):
                val = board[c][r]
                if val == '.':
                    continue
                elif val in cols:
                    return False
                else:
                    cols.add(val)

        # grid:
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (square//3) * 3 + i
                    c = (square % 3) * 3 + j
                    val = board[r][c]
                    if val == ".":
                        continue
                    if val in seen:
                        return False
                    seen.add(board[r][c])
        
        return True