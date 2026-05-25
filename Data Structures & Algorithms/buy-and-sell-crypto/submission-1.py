class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0

        for l in range(0, len(prices)):
            for r in range(l+1, len(prices)):
                p = prices[r] - prices[l]
                max_p = max(max_p, p)

        return max_p





        