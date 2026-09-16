class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

#comments

# in-place sorting
# no buil int sorting

#[1,2,1]
        count_element=[0] * (max(nums)+1)

        for i in nums:
            count_element[i] += 1

        start_index=0
        for i in range(len(count_element)):
            for j in range(start_index, start_index + count_element[i]):
                nums[j]=i
            start_index = start_index + count_element[i]






        