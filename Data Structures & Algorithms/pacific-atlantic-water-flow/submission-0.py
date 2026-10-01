class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        neigh = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(heights), len(heights[0])
        res = []
        atl, pac = set(), set()
        
        def dfs(r, c, prev_height, visited):
            for n in neigh:
                new_r, new_c = r + n[0], c + n[1]
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and heights[new_r][new_c] >= prev_height:
                    visited.add((new_r, new_c))

                    dfs(new_r, new_c,heights[new_r][new_c], visited)
                #think about the return conditions
            
            return

            
    
        # traverse for atlantic

        for i in range(rows):
            atl.add((i, cols-1))
            dfs(i, cols-1, heights[i][cols-1], atl)

        for j in range(cols):
            atl.add((rows-1, j))
            dfs(rows-1, j, heights[rows-1][j], atl)

        # traverse for pacific

        for i in range(rows):
            pac.add((i, 0))
            dfs(i, 0, heights[i][0], pac)

        for j in range(cols):
            pac.add((0, j))
            dfs(0, j, heights[0][j], pac)
            

        for i in range(rows):
            for j in range(cols):
                if (i, j) in atl and (i, j) in pac:
                    res.append([i,j])
        return res



        

# clarifications:

# 1. We cannot have the netige height? under the ocean level?
# Answer: No

# 2. Definition of Pacific and atalntic border:
#     if we reach to col == 0 or row == 0:
#         then Pacific
#     if row == len(heights) or col = len(heights[0]):
#         then Atlantic
# 3. Where to start?
#     Brute Force: have a nested loop to check al the cells 




