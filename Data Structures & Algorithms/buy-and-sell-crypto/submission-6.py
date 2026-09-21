class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """l=0
        d = len(prices) -1
        maxprofit =0
        dp = []

        while l<d:
            if prices[l+1] < prices[l]:
                l+=1
            elif prices[d-1]>prices[d]:
                d-=1
            else:
                maxprofit = max(maxprofit,prices[d] -prices[l] )
                l+=1
                d-=1
        
        id_sell = 1
        id_buy = 0

        for i in range(1,len(prices)-1):
            if prices[id_sell+1]>prices[id_sell]:
                id_sell+=1
            elif prices[id_buy+1]<prices[id_buy] and :
                id_buy +=1

        return max(0, prices[id_sell] -prices[id_buy])"""
        maxi=0
        n = len(prices)
        for i in range(n):
            for k in range(i,n):
                maxi = max(prices[k] - prices[i],maxi)
        return maxi
