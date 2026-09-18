class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_heap = []
        res = []

        for x, y in points: #O(n)
            dist = -(x**2 + y**2)
            if len(k_heap) < k:
                heapq.heappush(k_heap,(dist, x, y))
            elif -k_heap[0][0] > -dist:
                heapq.heappop(k_heap)
                heapq.heappush(k_heap, (dist, x, y))

        return [[x,y] for _, x, y in k_heap]

            




# points = [[0,2],[2,2]], k = 1

# origin: 0, 0

# ditance: [2, 2.86] 

# dict {[0,2]: 2,[2,2]: 2.8 }

# sort the dict by values
# get the top k keys

# time comp

        