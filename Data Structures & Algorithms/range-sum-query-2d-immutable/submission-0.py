class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        row = len(matrix)
        col = len(matrix[0])
        self.prefix = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            total = 0
            for j in range(col):
                total += matrix[i][j]
                self.prefix[i][j] = total
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rec_sum = 0
        if col1 == 0:
            for i in range(row2-row1+1):
                rec_sum = rec_sum + self.prefix[row1 + i][col2]
            return rec_sum

        elif col1 > 0 :
            for i in range(row2-row1+1):
                rec_sum = rec_sum + self.prefix[row1 + i][col2] - self.prefix[row1 + i][col1-1]
            return rec_sum        
        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)