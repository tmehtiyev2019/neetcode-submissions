class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = 1
        max_rate = max(piles) #time comp: O(n)

        out = max_rate

        if not piles:
            return 0

        while min_rate <= max_rate:
            mid = (min_rate + max_rate) // 2
            # compare if this rate we can complete eating bananas behore or after h hours
            t = 0
            for pile in piles:
                t += -(-pile//mid) #ceiling division
            if t > h:
                min_rate = mid + 1
            elif t <= h:
                max_rate = mid -1
                out = min(mid, out)
                
        return out

# time comp: log(m)*n where m is the ma value in the piles, and n is the lenght of the piles array
# space comp: O(1)





# (1:max(piles))


# edge cases:
# 1. empty list
# 2. only 1 calue

# Input: piles = [1,4,3,2], h = 9

# Output: 2

# minimum rate


# max(piles)/(h//len(piles))) = 2


# 25/(4//4)







        