class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_profit = 0
        min_value = 99999999
        for i in range(0, len(prices)):
            if min_value > prices[i]:
                min_value = prices[i]
            if prices[i]- min_value > mx_profit:
                mx_profit = prices[i] - min_value
        return mx_profit
        