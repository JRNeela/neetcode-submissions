class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, curr):
            if len(nums) == len(curr):
                ans.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(nums, curr)
                    curr.pop()
        ans = []
        curr = []
        backtrack(nums, curr)
        return ans
        
        