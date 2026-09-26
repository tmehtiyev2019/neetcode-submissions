class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        memo = {}

        def tar(i,total):

            if i == len(nums): 
                return 1 if total == target else 0

            if (i, total) in memo:
                return memo[(i, total)]

            res = tar(i+1, total - nums[i]) + tar(i+1, total + nums[i])
      
            memo[(i, total)] = res
            return res
        
        return tar(0, 0)


# Input: nums = [2,2,2], target = 2

# Output: 3


# operators:
# -, +


# res= 


