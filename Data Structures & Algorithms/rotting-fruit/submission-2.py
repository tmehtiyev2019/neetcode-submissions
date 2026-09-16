class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        m = -1
        fresh = 0

        #loop to lookup rotten (2) values in grid

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh = 1
        if not q:
            if fresh:
                return -1
            return 0

        while q:
            r, c, m = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                    q.append((nr, nc, m + 1))
                    visited.add((nr, nc))

        # to see if any fresh fruit is left            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    return -1
        return m 

        # time: O(mn), space: O(mn)
        # edge cases: 
            # all are rotten: 0
            # all are empty: 0
            # all are fresh : -1

        







# BFS will take care of the min--> queue
# how will we make sure that we still have/dont have any fresh fruit in the end?
# one teh que is empty, we will go over teh matric in a loop again (O(m*n), if we find any value with 1 we will return -1, else m
        