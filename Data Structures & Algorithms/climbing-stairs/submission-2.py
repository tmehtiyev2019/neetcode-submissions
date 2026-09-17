class Solution:
    memo = {1:1, 2: 2}
    def climbStairs(self, n: int) -> int:
        # if n in self.memo:
        #     return self.memo[n]        
        # res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # self.memo[n]=res
        # return res

        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return a


# time comp: O(n)
#space comp: O(n)



    


        