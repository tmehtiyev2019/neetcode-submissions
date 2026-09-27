class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # brut Force Approach:

        # # edge cases: if list is empty

        # if len(nums) == 0:
        #     return 0

        # maxSum = nums[0]
        # for i in range(len(nums)):
        #     temp_sum = 0
        #     for j in range(i, len(nums)):
        #         temp_sum += nums[j]
        #         maxSum = max(maxSum,temp_sum)
        # return maxSum

        # # complexity: O(n^2)
        # # space: O(1)



#optimized version
# Input: nums = [2,-3,4,-2,2,1,-1,4]

# Output: 8


# everytime we check the previous cumulative sum:
#     if it is negative we skip previous cumulative sum and strt form the new index
#     otherwise, we add th sum to the curren tindex value and fid the maxSum so far


        if len(nums) == 0:
            return 0

        curSum = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            curSum = max(curSum, 0)
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum

        # # complexity: O(n)
        # # space: O(1)








        