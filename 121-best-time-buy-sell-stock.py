class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy low
        r = 1 # sell high

        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                # in case we find a new minimum further than one index away
                l = r
            r += 1

        return max_profit

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for p in prices:
            profit = p - min_price
            max_profit = max(max_profit, profit)
            min_price = min(p, min_price)

        return max_profit

