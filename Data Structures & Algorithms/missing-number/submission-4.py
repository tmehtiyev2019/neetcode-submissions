# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for i in range(len(nums)+1):
#             if i not in nums:
#                 return i

# Brute Force approach
# time comp: n^2 n is the length of the nums array
# space O(1)


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         num_set=set(nums) 
#         for i in range(len(nums)+1):
#             if i not in num_set:
#                 return i

# # Brute Force approach
# # time comp: O(n) n is the length of the nums array
# # space O(n)



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_range = 0 # O(1)
        for i in range(len(nums)+1): #O(n)
            sum_range += i
        res = sum_range - sum(nums) #O(n)
        return res


# Brute Force approach
# time comp: O(n) n is the length of the nums array
# space O(1)
        