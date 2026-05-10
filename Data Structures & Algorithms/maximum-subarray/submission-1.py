'''
as soon as the total sum is negative, we can decrement the left
--> 

create sliding window to and iterat XX

We need to use kadane's algorithm
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSub = nums[0]
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub
            
        
        
        