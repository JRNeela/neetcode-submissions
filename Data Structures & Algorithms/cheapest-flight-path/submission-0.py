from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        dist = [[float('inf')] * (k+2) for i in range(n)]
        dist[src][0] = 0
        for u, v, cost in flights:
            adj[u].append((cost, v))

        pq = []
        heappush(pq, (0, src, 0))
        while pq:
            t_cost, stop, num_stops = heappop(pq)
            if stop == dst:
                return t_cost
            if num_stops > k:
                continue
            if t_cost > dist[stop][num_stops]:
                continue
            for cost, v in adj[stop]:
                if cost + t_cost < dist[v][num_stops + 1]:
                    dist[v][num_stops + 1] = cost + t_cost
                    heappush(pq, (cost + t_cost, v, num_stops + 1))
        return -1