# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n - 1 == 0:
#             return nums[0]
#         elif n - 1 == 1:
#             return max(nums[0], nums[1])
#         else:
#             return max(nums[n-1]+self.rob(nums[0:n-2]),self.rob(nums[0:n-1]))



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        
        
        memo = {0: nums[0], 1: max(nums[0], nums[1])}
        n = len(nums)
        def dp(i):
            if i in memo:
                return memo[i]
            else:
                res = max(nums[i]+dp(i-2),dp(i-1))
                memo[i] = res
                return res
        return dp(len(nums)-1)


#final time: O(n) and space: O(n)
#edge case: [10,2,3,15,8]
#for a given nums[i] : max(nums[i-1], nums[i], nums[i+1])
#calcualte teh max[i]: maximum amount you cna get till ith index
#recursion with the base case: nums[0], nums[1]--> nums[2]=max(nums[1], nums[0]+nums[2])



        