# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         map={}
#         out=[]
#         for item in nums:
#             map.get(item, 0) + 1
#         top_k_keys = sorted(map, key=map.get, reverse=True)[:k]
#         for key in top_k_keys:
#             out.append(key)
#         return out




# freq_dict = {
#     1:1,
#     2:2,
#     3:3
# }


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = defaultdict(int)
        heap = []
        res = []

        for num in nums:
            freq_dict[num] += 1
            
        for key, val in freq_dict.items(): #O(n)
            if len(heap)<k:
                heapq.heappush(heap, (val, key)) #O(logn)
            else:
                if val > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (val, key))
        
        for freq, num in heap:
            res.append(num)

        return res


# total: O(nlogn)





# q: is the input ordered?
# a: not