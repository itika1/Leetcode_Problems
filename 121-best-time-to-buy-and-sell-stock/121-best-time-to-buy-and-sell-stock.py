class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0 #buy
        r=1 #sell
        maxP=0
        while r<len(prices):
            curP=prices[r]-prices[l]
            if prices[l]<prices[r]:
                maxP=max(maxP,curP)
            else:
                l=r
            r+=1
            
        return maxP
            