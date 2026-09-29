class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:   
        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L += 1
        return L


# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         unique_set = sorted(set(nums))
#         nums[:len(unique_set)] = unique_set
#         return len(unique_set)

        


# Input: nums = [2,10,10,30,30,30]

# Output: [2,10,30]