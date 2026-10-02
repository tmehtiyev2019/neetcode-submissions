class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        zero_set = set()
        visited = set()
        no_replace = set()
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()

# To collect all the coord. of zeros
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    zero_set.add((i,j))


# # DFS recursion logic       
#         def dfs(r, c):
#             visited.add((r,c))
#             no_replace.add((r,c))
#             for i, j in neighbors:
#                 new_r, new_c = r + i, c + j
#                 if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == "O" and (new_r, new_c) not in visited:
#                     dfs(new_r, new_r)

#             return  
                

# to traverse all the zero values which cannot be replaced
        for i, j in zero_set:
            if (i== 0 or i== rows -1 or j== 0 or j== cols -1) and (i,j) not in visited:
                # dfs(i, j)
                q.append((i,j))
        
        while q:
            r, c = q.popleft()
            visited.add((r,c))
            no_replace.add((r,c))
            for i, j in neighbors:
                new_r, new_c = r + i, c + j
                if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == "O" and (new_r, new_c) not in visited:
                    q.append((new_r,new_c))



# to replace zeros with X
        for i, j in zero_set:
            if (i,j) not in no_replace:
                board[i][j] = "X"
