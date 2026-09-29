class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cum_sum = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            nums[i] = cum_sum

        for j in range(len(nums)):
            if j==0:
                left = 0
            else:
                left = nums[j-1]

            if j == len(nums)-1:
                right = 0
            else:
                right = nums[len(nums)-1] - nums[j]
            
            if left == right:
                return j
        return -1
    

            
        