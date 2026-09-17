class Solution:
    memo = {1:1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]        
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n]=res
        return res

# n = 1 --> out: 1
# n = 2 -- > out: 2
# n = 3 --> out: 3 --> n:1 + n:2

# Recursion with base condition:

# calc_step(n):
# memoization


    


        