class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-weight for weight in stones]
        heapq.heapify(stones) 
        while stones:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
            else:
                return -x
            if -x < -y:
                heapq.heappush(stones, y - x)
            elif -x > -y:
                heapq.heappush(stones, x - y)
        return 0



# Base condition: 
# no more than 1 stone remaining: 
# return the weight of last remaining stone or 0 if none remain.
        