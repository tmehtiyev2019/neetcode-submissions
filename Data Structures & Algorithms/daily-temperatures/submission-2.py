class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):  
            while stack and temperatures[i] > stack[-1][0]:
                val, ind = stack.pop()
                res[ind] = i - ind
            stack.append([temperatures[i], i])
        return res


# Input: temperatures = [30,38,30,36,35,40,28]

# Output: [1,4,1,2,1,0,0]


