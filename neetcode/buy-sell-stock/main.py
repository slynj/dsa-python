# https://neetcode.io/problems/buy-and-sell-crypto

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while (l < r and r < len(prices)):
            if prices[l] > prices[r]: 
                l = r
            else:
                maxP = max(maxP, prices[r] - prices[l])

            r += 1
        
        return maxP