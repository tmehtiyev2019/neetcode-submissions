class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        path = []
        candidates.sort() 
        def dfs(start, total):

            if total == target:
                comb.append(path.copy())
                return
    
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i]> target:
                    break
                path.append(candidates[i])
                dfs(i+1, total + candidates[i])
                path.pop()
        dfs(0,0)
        return comb
        