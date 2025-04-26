class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = l + 1

        while l < len(prices) - 1 and r < len(prices):
            profit = max(profit, prices[r] - prices[l])

            if prices[l] < prices[r]:
                r += 1
            else:
                l = r
                r = l + 1
        return profit

