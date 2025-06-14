class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        mx_profit = 0
        min_profit = float("inf")
        for i in range(0, n):
            min_profit = min(min_profit, prices[i])
            mx_profit = max(mx_profit, prices[i] - min_profit)
        return mx_profit


c1 = Solution()
c1.maxProfit(prices=[7, 1, 5, 3, 6, 4])
