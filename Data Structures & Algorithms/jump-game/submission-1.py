class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def jump(i):
            if i in memo:
                return memo[i]

            res = False

            if nums[i] == 0 and i != len(nums) - 1:
                return False
                
            if i >= len(nums):
                return False

            if i == len(nums) - 1:
                return True

            for j in range(1, nums[i]+1):
                res = res or jump(i+j)
            memo[i] = res
        
            return memo[i]

        return jump(0)




# two main conditions : zero
# the out of range

# edge cases:
# 1, 2, 2, 0, 0


# i = i + nums[i] -->1
# -->3


# maximum 
        