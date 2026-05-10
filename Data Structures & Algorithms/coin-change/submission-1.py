class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        rows = len(coins)
        cols = amount + 1
        for i in range(rows):
            for c in range(coins[i], cols):
                skip = dp[c]
                take = float('inf')
                if c - coins[i] >= 0:
                    take = 1 + dp[c - coins[i]]
                dp[c] = min(skip, take)
        return dp[amount] if dp[amount] != float('inf') else -1
        