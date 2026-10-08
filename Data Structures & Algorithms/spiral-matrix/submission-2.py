class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.rows, self.cols = len(matrix), len(matrix[0])
        self. visited = set()
        self.neighbors = [[0,1], [1,0], [0,-1], [-1,0]]
        self.res = []


        def dfs(i, j, ni, nj):

            self.res.append(matrix[i][j])
            self.visited.add((i,j))

            if i + ni >= 0 and i + ni < self.rows and j + nj >= 0 and j + nj < self.cols and (i + ni, j + nj) not in self.visited:
                dfs(i + ni, j + nj, ni, nj)


            for di, dj in self.neighbors:
                if i + di < 0 or i + di >= self.rows or j + dj< 0 or j + dj >= self.cols or (i + di, j + dj) in self.visited:
                    continue
                dfs(i + di, j + dj, di, dj)
            return


        dfs(0, 0, 0, 1)
        return self.res

# time complexity: rows * cols
# space complexity: rows * cols : think about this


        