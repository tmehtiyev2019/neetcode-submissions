class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        seen = set()
        ans = 0
        for i, num in enumerate(nums):
            if num not in seen:
                if num - 1 in check:
                    # num is not start point, so move on
                    continue
                
                # num is a possible seq starting point
                count = 0
                while  num in check:   
                    count += 1
                    seen.add(num)
                    num += 1
                ans = max(ans, count)

        return ans

            

            

        
        