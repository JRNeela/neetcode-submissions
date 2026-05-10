'''
different denominations of coins

amount --> return fewest number of coins needed to reach amount


let dp[i] represent the minimum number of coins needed to form the amount i 

diff = i - coin >= 0 --> dp[i] = 1 + dp[i - coin]
if not --> 

attach the value of 1 to each coin amount listed
set dp[0] to 0


'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount + 1)]
        n = amount
        dp[0] = 0
        for i in range(1, n+1):
            for coin in coins:
                diff = i - coin
                if diff >= 0:
                    dp[i] = min(dp[i], 1 + dp[diff])
        return dp[n] if dp[n] != float('inf') else -1


        