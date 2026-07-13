from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        how many connected islands of '1's are there in grid?
        we traverse grid, each cell in 4 directions.
        so while at an island, if we don't find any connected 1s anymore, increment island count += 1
        """

        islands = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    visited.add((r, c))
                    q = deque([(r, c)])
        
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions: # nr, nc = 0 + 1, 0 + 1 = (0, 1), (0, -1)
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                q.append((nr, nc))

        return islands