class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0

        for p in prices:
            buy = min(p, buy)
            profit = p - buy

            best = max(best, profit)
        return best