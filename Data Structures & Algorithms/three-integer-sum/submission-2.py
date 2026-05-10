# Three distinct numbers where nums[i] + nums[j] + nums[k] == 0
#     - all add up to 0
# output should not contain duplicates
#     - specific ordering --> once seen, we pass on it (default ordering)
#     - set()

# 3 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5
#     -numbers can be negative

# nums = [-1,0,1,0,-1,-4]
# nums = [-4, -1, -1, 0, 0, 1]
# sort the array
#     - this will allow us to run a two pointer search solution

# sum = 0 
# 0 - (-1) = 1
# if nums[i] + sum(j, k) == 0: 
#     we know that we have a match
# sum => two pointers

# run two pointer from i + 1 to len(nums) - 1
#     - we wont need to waste time here on unecessary calcuations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums)):
            #we have encountered a duplicate iteration, we move forward
            if i > 0 and nums[i -1] == nums[i]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return ret
                



        