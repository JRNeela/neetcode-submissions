
'''

[5,5,3],
[2,3,6],
[1, 1, 1]


let path(i,j) represent the longest path at matrix[i][j]

we can either move up, left, right, down or end
let curr represent our current path 
if matrix[i+1][j] has the next value (curr + 1), we then check out matrix[i+1][j] and increase count by 1

same can be repeated for all the directions,
if no direction is found, we end our path 

after exiting our current path, we then check to see if the path is bigger than our max path

dfs --> parameters are i, j and the path []

iterate through the matrix row to n, col to n

store the longest paths at each node in our cache so that we dont need to call the function every time

evaluate whichever path was the better one

'''
from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_path = 0
        n = len(matrix)
        # path_count = [[float('-inf')] * n ] * n
        def check_in_bounds(i, j):
            return (0 <= i < len(matrix)) and (0 <= j < len(matrix[0]))

        @cache
        def dfs(r, c):
            # explore all four and then return the largest value as our value for [i][j]
            dirs = [(0,1), (1, 0), (-1, 0), (0, -1)]
            #check to see if we can keep making the path longer
            max_len = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if check_in_bounds(nr, nc) and matrix[nr][nc] > matrix[r][c]:
                   max_len = max(max_len, 1 + dfs(nr, nc))
            return max_len
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_path = max(max_path, dfs(i, j))
        return max_path
         
                    



        