class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        currMin = 0
        globalMax = nums[0]
        globalMin = nums[0]
        total = 0


        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
            total += n
        return max(globalMax, total - globalMin) if globalMax >= 0 else globalMax


        # n = len(nums)
        # maxSum = nums[0]

        # for i in range(len(nums)):
        #     currSum = 0
        #     for j in range(i, i+n):
        #         currSum += nums[j % n]
        #         maxSum = max(maxSum, currSum)
        # return maxSum










# Input: nums = [-2,4,-5,4,-5,9,4]

# Output: 15


# chanelelges:

# where to start
# how to claculate teh prev sum (consdirein that one index cannot be repearetd inthe subarry, we can consider the of of all other indexes int he array as prev sum)
# the issue is: will w ejust sum all toher index and assign it as prev su. or we will ahve specifi method for it?


        # if len(nums) == 0:
        #     return 0

        # n = len(nums)
        # start_index = 0
        # curSum = 0
        # maxSum = nums[0]

        # for i in range(0, -len(nums)):
            
        #     if i != 0:
        #         if start_index == (i + n) % n:
        #             curSum -= nums[start_index]
        #             start_index = (start_index - 1 + n) % n
        #     if curSum < 0:
        #         curSum = 0
        #         start_index = (i- 1 + n) % n

        #     curSum += nums[(i + n) % n]
        #     maxSum= max(maxSum,curSum )
        # return maxSum


        