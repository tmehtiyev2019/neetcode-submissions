class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #edge cases:
        rows, cols = len(matrix), len(matrix[0])
        
        left = 0
        right = rows*cols - 1

        while left <= right:
            mid = (left + right)//2
            if matrix[mid//cols][mid%cols] > target:
                right =  mid - 1
            elif matrix[mid//cols][mid%cols] < target:
                left = mid + 1
            else:
                return True
        return False
            



        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        