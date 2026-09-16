class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
                return -1
        visited = set()
        q = deque()
        q.append((0,0,1))
        visited.add((0,0))
        length = 1
        neighbors = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]

        while q:
            r, c, l = q.popleft()
            if grid[r][c] == 0 and r == rows - 1 and c == cols - 1:
                return l
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == 0:
                    q.append((nr, nc, l + 1))
                    visited.add((nr, nc))
        return -1
                

    


# Input: grid = [
#     [0,1,0],
#     [1,0,0],
#     [1,1,0]
# ]

# Output: 3



# grid=[
# [0,1,0],
# [1,0,0],
# [1,1,0]]