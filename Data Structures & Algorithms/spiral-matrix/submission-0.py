class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.rows, self.cols = len(matrix), len(matrix[0])
        self. visited = set()
        self.neighbors = [[0,1], [1,0], [0,-1], [-1,0]]
        self.res = []


        def dfs(i, j, ni, nj):
            
            if i < 0 or i >= self.rows or j< 0 or j >= self.cols or (i,j) in self.visited:
                return

            self.res.append(matrix[i][j])
            self.visited.add((i,j))

            dfs(i + ni, j + nj, ni, nj)


            for di, dj in self.neighbors:
                dfs(i + di, j + dj, di, dj)
            return


        dfs(0, 0, 0, 1)
        return self.res




        