# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for i in range(len(nums)+1):
#             if i not in nums:
#                 return i

# Brute Force approach
# time comp: n^2 n is the length of the nums array
# space O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set=set(nums) 
        for i in range(len(nums)+1):
            if i not in num_set:
                return i

# Brute Force approach
# time comp: O(n) n is the length of the nums array
# space O(n)
        