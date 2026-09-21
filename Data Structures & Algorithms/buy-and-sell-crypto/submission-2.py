class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # min price we have seen so far
        min_price = float('inf')
    
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            curr_profit = prices[i] - min_price
            max_profit = max(curr_profit, max_profit)

        return max_profit

# max price we have seen so far
# min price we have seen so far
# min price shoudl come before max price
# what if we also store the index as well
# or everytim we find a 