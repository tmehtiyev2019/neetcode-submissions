class Solution:
    def countBits(self, n: int) -> List[int]:
        out= []
        for num in range(n+1):
            res = 0
            while num:
                res += 1 & num
                num = num >> 1
            out.append(res)
        return out

        