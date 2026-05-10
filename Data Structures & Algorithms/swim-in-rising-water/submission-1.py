import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:        
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        dist[0][0] = grid[0][0]
        while heap:
            time, r, c = heapq.heappop(heap)
            if time > dist[r][c]:
                continue
            dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_dist = max(time, grid[nr][nc])
                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist
                        heapq.heappush(heap, (new_dist, nr, nc))
        return dist[m-1][n - 1]