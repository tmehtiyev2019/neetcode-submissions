class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        nums = [i for i in range(1,n+1)]
        def dfs(start, path):
            if len(path) == k:
                comb.append(path.copy())
                return
            
            for j in range(start, len(nums)):
                path.append(nums[j])
                dfs(j+1, path)
                path.pop()
        dfs(0,[])
        return comb



# nums = [1,2,3]
# ind = 0 -- >[1]



        