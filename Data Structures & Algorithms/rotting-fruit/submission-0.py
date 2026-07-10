from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        for each cell [2], check 4 directions, if there is a [1], change it to [2]
        increment minute count += 1 (each level)
        traverse connected cells using a BFS
        if at end of traversal there is still a cell with [1], return -1 (can't rot all oranges)
        """
        row, cols = len(grid), len(grid[0])
        fresh = 0    
        q = deque()

        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 2:
                    # run bfs
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        print(fresh)
        if fresh == 0:
            return 0
        
        # 4 directions:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        mins = 0

        # BFS using a q (FIFO)
        while q and fresh > 0:
            # process q level by level:
            mins += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        print(fresh) # still 2 fresh
        return mins if fresh == 0 else -1


        
                