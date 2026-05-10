'''
we need to implement a DP solution bc return the maximum amounf of money
without alerting the police
--> no apparent greedy solution

tabulation, memoization

choices:
    - I can either rob the house i and skip the house i+1
    - I can skip the house

tabulation

initialize a single dp array of 0 --> n
determine the maximum amount of money I can earn at each specific house

return the tab[n-1] value

max(tab[i-1], nums[i] + tab[i-2])

THE KEY: Need to know when it is necessary to begin a problem with a cushion of 0's
and when not to 


'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        tab = [0] * n
        tab[0] = nums[0]
        tab[1] = max(nums[0], nums[1])
        for i in range(2, n):
            tab[i] = max(tab[i-1], nums[i] + tab[i-2])
        return tab[n -1]
        


        