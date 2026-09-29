class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        k = 0
        for R in range(1, len(nums)):
            if nums[R] == nums[R-1] and k < 1:
                nums[L] = nums[R]
                L += 1
                k += 1
            elif nums[R] != nums[R-1]:
                nums[L] = nums[R]
                k = 0
                L += 1
        return L




# Notes:
# 1. sorted in non-decreasing order,
# 2. In place opr. -- > most twice
# 3. relative order the same
# 4. modifying the input array in-place with O(1) extra memory.
        