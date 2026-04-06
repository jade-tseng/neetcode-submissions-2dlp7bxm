class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # init counter
        # traverse the grid
        # flood-fill already visited cells and add to counter

        if not grid:
            return 0
        
        count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # if out of bounds on grid, stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0' # set it to 0 after visiting
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        
        return count

        # # scan whole grid:
        # if grid[r][c] == '0':
        #     pass
        # if grid[r][c] == '1':
        #     count += 1
        
        # # once you find 1, start from (r, c), explore all connected 1s:
        # # check 4 neighbors:


        #dfs() -> if out of bounds on grid, stop, 