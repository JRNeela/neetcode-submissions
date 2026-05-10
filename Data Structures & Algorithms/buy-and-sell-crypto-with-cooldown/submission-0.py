'''
* After you sell you coin, you cannoth buy another one on
the next day (cooldown of one day)
* You may only own one neetcoin at a time 

return the maximum profit you can achieve

we need to think about the decision tree for these kinds of problesm

we can only be in the state to sell or buy understanding that we can only hold one item at a time
additionally, we know that we always have the option to pause (do nothing) which we can always do

buy/sell --> boolean
cache dp --> hold our previous recursive calls for our state ((i, buying/selling), max_profit)

if we buy or do nothing, we need to iterate i+1
if we sell, we need to iterate i+2

sell = add current price
buy = subtract current price
do nothing = nothing

go through decisions accordingly, return dfs[0, buying = true]

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)