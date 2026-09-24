class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort() #n log(n)
        return nums[-k]


# Input: nums = [2,3,1,5,4], k = 2

# Output: 4

# # brute force approach:
# nums.sort() #n log(n)
# return nums[k-1]
# #space comp: O(1)


# edge cases:
# 1. nums is empty
# 2. len(nums) < 2


# [1,2,2,2,3] k=3
# res = 2


# Input: nums = [2,3,1,1,5,5,4], k = 3

# Output: 4

# sorted_num = [1, 1, 2, 3, 4, 5, 5], k = 3


        