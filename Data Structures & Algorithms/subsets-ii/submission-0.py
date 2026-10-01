
# BRute Force Approach
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        comb = set()
        def dfs(i, subset):
            if i >= len(nums):
                comb.add(tuple(subset))
                return 

            
            # with index i
            subset.append(nums[i])
            dfs(i+1, subset)

            # without index i
            subset.pop()
            dfs(i+1, subset)
        dfs(0,[])
        return [list(s) for s in comb]


# nums = [1, 1, 2]


# []--> [1], -->[1, 1] --> [1, ]

        