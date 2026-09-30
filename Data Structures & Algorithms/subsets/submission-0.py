class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >=len(nums):
                res.append(subset.copy())
                return

            #call without index i
            dfs(i+1)

            #call with index i
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()

        dfs(0)
        return res
          

# Input: nums = [1,2,3]

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]




        