class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        substr = ""
        directions = [[0,1], [0,-1], [-1, 0], [1, 0]]
        def backtrack(substr, row, col):
            if row >= rows or col >= cols or row < 0  or col < 0:
                return False
            substr += board[row][col]
            print(substr)
            if substr == word:
                return True
            if len(substr) >= len(word):
                return False
            for x, y in directions:
                nx, ny = x + row, y + col
                if (nx, ny) not in visited:
                    visited.add((row, col))
                    if backtrack(substr, nx, ny):
                        return True
                    visited.remove((row, col))
        for row in range(rows):
            for col in range(cols):
                visited = set()
                if backtrack("", row, col):
                    return True
        return False
            
                
            
        