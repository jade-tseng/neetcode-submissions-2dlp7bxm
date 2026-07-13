class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()

        current_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    q = deque([(r, c)])
                    area = 1
                
                    while q:
                        r, c = q.popleft()
                        # visit neighbors:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1  and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                q.append((nr, nc))
                                area += 1

                    current_area = max(area, current_area)
        
        return current_area