class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            res = self.sumOfSquares(n)
            if res == 1:
                return True
            if res in visited:
                return False
            visited.add(res)
            n = res
           

    def sumOfSquares(self, n):
        output  = 0

        while n:
            digit = n % 10
            digit  = digit**2
            output += digit
            n = n // 10
        return output
    





# Def of non-cyclical number:

# 1. 
        