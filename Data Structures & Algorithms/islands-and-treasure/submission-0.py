class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

      rows, cols = len(grid), len(grid[0])
      directions = [[0,1], [1,0], [0,-1], [-1,0]]
      visited = set()
      q = deque()
      for i in range(rows):
        for j in range(cols):
          if grid[i][j] == 0:
            q.append([i,j,0])
            visited.add((i,j))
      while q:
        i, j, cost = q.popleft()
        for d in directions:
          new_row, new_col = i + d[0], j + d[1]
          if  0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != -1 and (new_row, new_col) not in visited:
            grid[new_row][new_col] = cost + 1
            q.append([new_row, new_col,cost + 1])
            visited.add((new_row, new_col))


# time comp: O(mxn)
# space comp: O(mxn)







# i, j for rows and colums
# for each i,j we need to check if the INF
# if INF we will find the distance for 0 --> min distance

# how to find the minimum distance?

# starting point to update the distance


# i, j = 0, 0 # rows and colums



# for i

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

        