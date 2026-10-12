class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0

        for p in prices:
            if p < buy:
                buy = p
            if best < (p - buy):
                best = p - buy
        return best