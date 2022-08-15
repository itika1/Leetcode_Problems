class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs_visit(grid, u):
            i, j = u[0], u[1]
            visit.add((i,j))
            if i > 0 and grid[i-1][j] == '1' and (i-1,j) not in visit:
                dfs_visit(grid, (i-1,j))
            if i < height - 1 and grid[i+1][j] == '1' and (i+1,j) not in visit:
                dfs_visit(grid, (i+1,j))
            if j > 0 and grid[i][j-1] == '1' and (i,j-1) not in visit:
                dfs_visit(grid, (i,j-1))
            if j < width - 1 and grid[i][j+1] == '1' and (i,j+1) not in visit:
                dfs_visit(grid, (i,j+1))
        
        if len(grid) == 0:
            return 0
        count = 0
        visit = set()
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1' and (i,j) not in visit:
                    dfs_visit(grid,(i,j))
                    count += 1
        return count
        