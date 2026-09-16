class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue=deque()
        visited=set()
        area=[0]
        area_size=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited: 
                    queue.append((i, j))
                    visited.add((i, j))
                    area_size=1
                    while queue:   
                        r, c = queue.popleft()
                        # icrement the size by one and add to the visited set
                        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                                queue.append((nr, nc))
                                area_size += 1
                                visited.add((nr, nc))
                    area.append(area_size)
                            

        return max(area)

# time complexity: O(nm+m)



        


# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]

# Output: 6



# 1. how to define the island?
# 2. how many islands do we have: push them into queue
# 3. traverse the island to find the size: DFS or BFS
# 4. store the sizes
# 5. find max number in the stored data
