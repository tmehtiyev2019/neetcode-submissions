class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    q.append((i,j))
        while q:
            i, j = q.popleft()
            for c in range(cols):
                matrix[i][c] = 0
            for r in range(rows):
                matrix[r][j] = 0



# Time complexity: O(m*n*(m+n))
# Spce complexity: O(m*n)



        
        