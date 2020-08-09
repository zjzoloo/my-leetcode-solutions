# Runtime: 32 ms
# Memory Usage: 14 MB

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)


# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        a, b, c = 0, -prices[0], 0
        for i in range(1, len(prices)):
            tmp = a
            a = max(a,c)
            c = b+prices[i]
            b = max(b, tmp-prices[i])
        return max(a,c)
        
