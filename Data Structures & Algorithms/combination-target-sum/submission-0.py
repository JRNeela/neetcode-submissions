class Solution:
    '''
    add each number
    '''
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        subset = []
        def dfs(index):
            if sum(subset) == target:
                ret.append(subset.copy())
                return
            elif index >= len(nums) or sum(subset) > target:
                return   
            subset.append(nums[index])
            #this above means that we are spamming one number
            dfs(index)
            subset.pop()
            #this below means that we are moving to the next number to spam
            dfs(index+1)
        dfs(0)
        return ret
        


            


        

        