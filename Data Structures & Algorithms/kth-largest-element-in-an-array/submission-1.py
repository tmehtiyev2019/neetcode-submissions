class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return heap[0]
            



        # nums.sort() #n log(n)
        # return nums[-k]



# max = -10000

# # Input: nums = [2,3,1,5,4], k = 3

# min heap
# sorted_top_k_stack = [4, 3, 5]
# return sorted_top_k_stack[0]



# Output: 4

# # brute force approach:
# nums.sort() #n log(n)
# return nums[k-1]
# #space comp: O(1)


# edge cases:
# 1. nums is empty
# 2. len(nums) < 2
# 3. negative numbers


# [1,2,2,2,3] k=3
# res = 2


# Input: nums = [2,3,1,1,5,5,4], k = 3

# Output: 4

# sorted_num = [1, 1, 2, 3, 4, 5, 5], k = 3


        