class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_count = Counter(nums) # O(n)
        for i in num_count.keys():
            if num_count[i] > 1:
                return i
            
        