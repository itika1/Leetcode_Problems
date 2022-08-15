class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        maxprofit=0
        while right<len(prices):
            current_profit=prices[right]-prices[left]
            if prices[left]<prices[right]:
                maxprofit=max(current_profit, maxprofit)
            else:
                left=right
            right+=1
        return maxprofit
        