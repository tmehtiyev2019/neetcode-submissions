class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i

#brute Force approach
# time comp: n^2 n is the length of the nums array
# space O(1)
        