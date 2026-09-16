class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map={}
        for i in range(len(nums)):
            if nums[i] in target_map:
                return [target_map[nums[i]], i]
            else:
                target_map[target-nums[i]] = i
        
# nums = [3,4,5,6], target = 7

# target_map={}

# {4:0, 3:1, 2:2, 1:3}

