class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_p = math.inf
        # time O(n), space O(1)
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            res = max(res, prices[i]-min_p)
        
        return res