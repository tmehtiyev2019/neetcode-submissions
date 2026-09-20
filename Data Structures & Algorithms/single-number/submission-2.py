# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         heapq.heapify(nums)
#         while nums:
#             k = heapq.heappop(nums)
#             if len(nums) > 0:
#                 m = heapq.heappop(nums)
#             else:
#                 return k
#             if k != m:
#                 return k

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]





        