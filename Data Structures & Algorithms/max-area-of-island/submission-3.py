'''
how do I get the area of an island 
know when I hit water --> when I hit a zero, do not expand if 1 expand
if out of bounds do not expand 


how do I find the max island:


to count the ar
we will run a simple bfs

add the initial 1 and then all its neighbors, then run bfs on those
neighbors; after visiting a node we mark it as visited via a 0

we keep track of the reachable nodes via a queue,
while queue:
    popleft queue
    mark node as visited, increment curr_level by 1
    next searh the neighbors (within bounds) if any are 1 we add to the queue 
then we compare with out current max value and adjust

return the max values


'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search(i, j):
            ret_values = []
            dirs = [(0,1), (1, 0), (-1, 0), (0, -1)]
            for d in dirs:
                new_r, new_c = i + d[0], j + d[1]
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                    if grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 0
                        ret_values.append([new_r, new_c])
            return ret_values
        q = deque()
        n = len(grid[0])
        m = len(grid)

        max_island_size = 0
        for i in range(m):
            for j in range(n):
                #found a island, start a level search
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q.append([i, j])
                    current_island_size = 0
                    while q:
                        row, col = q.popleft()
                        current_island_size += 1
                        frontier_land = search(row, col)
                        for c in frontier_land:
                            q.append(c)
                    max_island_size = max(current_island_size, max_island_size)
                
        return max_island_size
        
                        

                
        