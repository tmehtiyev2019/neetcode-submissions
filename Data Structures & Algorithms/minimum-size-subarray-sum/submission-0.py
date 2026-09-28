class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0
        min_len = float("inf")
        exist_flag = True
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                exist_flag = False
                min_len = min(min_len, R - L + 1)
                total -= nums[L]
                L += 1
        if exist_flag:
            return 0
        else:
            return min_len