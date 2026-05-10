class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        [10, 11, 5, 6, 7, 1]

        loop through the array at every price at index
        see at the rest of the array if I make a profit
        if so,
        if the profit I make is greater than my previous highestProfit
        then I will change highestProfit to that profit
        else keep going through possible sell points
        if at all profit is 0 or less, 
        this is an indication that I have exhauseted profitabillity for that current buy day -> move to next buy day


        '''
        maxProfit = 0
        buyDay = 0
        sellDay = 0

        while sellDay < len(prices):
            profit = prices[sellDay] - prices[buyDay]
            if profit < 0:
                buyDay += 1
                continue
            elif profit > maxProfit:
                maxProfit = profit
            sellDay += 1
            
        return maxProfit
        