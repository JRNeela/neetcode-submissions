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
            newRob = 0
            house_two_down, house_one_down = 0, 0
            for house in li:
                newRob = max(house + house_two_down, house_one_down)
                house_two_down = house_one_down
                house_one_down = newRob
            return newRob
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))




        