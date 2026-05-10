'''
circle

no two at once: rob(i) --> i+2

maximum amount of money I have robbed until house i

traverese i --> n; rob


at house i, total = rob(i) - dp[i-2]

or total = dp[i-1]
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(li):
            n = len(li)
            if not li:
                return 0
            if len(li) == 1:
                return li[0]
            dp = [0] * n
            dp[0] = li[0]
            dp[1] = max(li[1], li[0])
            for i in range(2, n):
                dp[i] = max(dp[i-2] + li[i], dp[i-1])
            print(dp)
            return dp[n-1]
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))




        