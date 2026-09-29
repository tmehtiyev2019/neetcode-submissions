class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        L = 0
        R = 1
        prev = ""
        while R < len(arr):
            #write the turbulent logic
            if arr[R-1] < arr[R] and prev != "<":
                #update the length
                res = max(res, R - L + 1)
                R += 1
                prev = "<"
            elif arr[R-1] > arr[R] and prev != ">":
                res = max(res, R - L + 1)
                R += 1
                prev = ">"
            elif arr[R-1] == arr[R]:
                L = R
                R += 1
                prev = "="
            else:
                L = R - 1
                prev = ""
        return res



#         L = 0
#         max_len = 0

#         for R in range(len(arr)):


# Input: arr = [2,4,3,2,2,5,1,4]

# Output: 4







        