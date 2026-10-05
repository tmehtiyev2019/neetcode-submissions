# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         num_freq={}
#         out=[]
#         for item in nums:
#             num_freq[item] = num_freq.get(item, 0) + 1

#         res = []
#         arr = []
#         for num, count in num_freq.items():
#             arr.append((count, num))
#         arr.sort(key=lambda x: x[0])

#         c = 0
#         for count, num in arr[-k:]:
#             res.append(num)


#         return res

# time comp: O(nlogn)
# space comp: O(n)





# freq_dict = {
#     1:1,
#     2:2,
#     3:3
# }


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         freq_dict = defaultdict(int)
#         heap = []
#         res = []

#         for num in nums:
#             freq_dict[num] += 1
            
#         for key, val in freq_dict.items(): #O(n)
#             if len(heap)<k:
#                 heapq.heappush(heap, (val, key)) #O(logn)
#             else:
#                 if val > heap[0][0]:
#                     heapq.heappop(heap)
#                     heapq.heappush(heap, (val, key))
        
#         for freq, num in heap:
#             res.append(num)

#         return res


# total: O(nlogn)





# q: is the input ordered?
# a: not







#Bucket sort option



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = defaultdict(int)
        res = []

        for num in nums:
            freq_dict[num] += 1

        count_index = [[] for i in range(len(nums)+1)]
            
        for num, count in freq_dict.items():
            count_index[count].append(num)

        for i in range(len(count_index) - 1, 0, -1):
            for num in count_index[i]:
                res.append(num)
                if len(res) == k:
                    break
            if len(res) == k: 
                break

        return res