'''
start at the the ith step

let dp[n] represent the minimum cost to start at step n

goal: reach index n (n is the length of the list)

ith staircase:
- pay cost and move 1 step
- pay cost and move 2 steps

dp[n] = min(dp[n - 1] + cost, dp[n-2] + cost)

dp[1] = cost[1]
dp[0] = cost[0]

algo:
iterate from 2, len(end)
    fill in our table
only need to keep track of 2 variables
return dp[n+1]


'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[len(cost)]


        

        