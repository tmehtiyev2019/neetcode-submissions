class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix)
        new_martix = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(cols):
            for j in range(rows):
                new_martix[i][j] = matrix[j][i] 

        for i in range(cols):
            for j in range(rows):
                matrix[i][j] = new_martix[i][j]

        for i in range(rows):
            for j in range(cols):
                new_martix[i][j] = matrix[i][-1 - j]

        
        for i in range(cols):
            for j in range(rows):
                matrix[i][j] = new_martix[i][j]


        
        