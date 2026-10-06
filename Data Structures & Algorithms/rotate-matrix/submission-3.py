class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix)
        new_martix = [[0 for _ in range(rows)] for _ in range(cols)]
        converted = set()
        switched = set()

        for i in range(cols):
            for j in range(i + 1, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
     



        for i in range(rows):
            for j in range(cols//2):
                matrix[i][j], matrix[i][cols - 1 - j] = matrix[i][cols - 1 - j],  matrix[i][j]
   





        
        