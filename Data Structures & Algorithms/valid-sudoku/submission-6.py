class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                elif val in seen:
                    print("rows false")
                    return False
                else:
                    seen.add(val)
        
        for c in range(9):
            cols = set()
            for r in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                elif val in cols:
                    print("cols false")
                    return False
                else:
                    cols.add(val)
    
        for s in range(9):
            grid = set()
            for i in range(3):
                for j in range(3):
                    r = (s // 3) * 3 + i
                    c = (s % 3) * 3 + j
                    val = board[r][c]
                    if val == ".":
                        continue
                    elif val in grid:
                        print("grid false")
                        return False
                    else:
                        grid.add(val)
        
        return True
                        