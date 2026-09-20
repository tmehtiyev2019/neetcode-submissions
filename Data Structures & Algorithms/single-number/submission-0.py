class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        while nums:
            k = heapq.heappop(nums)
            if len(nums) > 0:
                m = heapq.heappop(nums)
            else:
                return k
            if k != m:
                return k

        