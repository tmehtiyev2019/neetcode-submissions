class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited=set()
        queue=deque()
        island_count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    island_count += 1
                    visited.add((i,j))
                    queue.append((i,j))
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nr, nc = dr + r, dc + c
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1' and (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                
        return island_count
