class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    numIslands += 1
                    grid[r][c] = "0"
                    neighbors = deque()
                    neighbors.append((r, c))
                    while neighbors:
                        row, col = neighbors.popleft()
                        if row > 0 and grid[row - 1][col] == "1":
                            neighbors.append((row - 1, col))
                            grid[row - 1][col] = "0"
    
                        if col > 0 and grid[row][col - 1] == "1":
                            neighbors.append((row, col-1))
                            grid[row][col - 1] = "0"
                        if row < rows - 1 and grid[row + 1][col] == "1":
                            neighbors.append((row + 1, col))
                            grid[row+1][col] = "0"
                        if col < cols - 1 and grid[row][col + 1] == "1":
                            neighbors.append((row, col + 1))
                            grid[row][col + 1] = "0"
        return numIslands
                        
