'''
we can store each of these distances in a heap and then pop the k-closest ones
'''
import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances_from_origin = []
        for point in points:
            x = point[0]
            y = point[1]
            distance_from_origin = math.sqrt(x**2 + y**2)
            distances_from_origin.append([distance_from_origin, x, y])
        heapq.heapify(distances_from_origin)
        ret = []
        for _ in range(k):
            distance_from_origin, x, y = heapq.heappop(distances_from_origin)
            ret.append([x, y])
        return ret



        