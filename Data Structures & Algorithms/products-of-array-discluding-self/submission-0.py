class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        res = []
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod = prod * num
        
        for i in nums:
            if zero_count > 1:
                res.append(0)

            elif i == 0:
                res.append(prod)

            elif zero_count == 1:
                res.append(0)

            else:
                res.append(prod//i)
        return res

                
                


# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
        