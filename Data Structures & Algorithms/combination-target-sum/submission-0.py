class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        comb = []
        path = []
        def dfs(i, total):
            if len(nums) == 0:
                return

            if total > target:
                return
            
            if total == target:
                comb.append(path.copy())
                return

            for j in range(i,len(nums)):
                path.append(nums[j])
                dfs(j, total + nums[j])
                path.pop()

        dfs(0, 0)
        return comb


        