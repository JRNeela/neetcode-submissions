
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        vals = set(nums)
        max_run = 0
        for num in vals:
            if num - 1 not in vals:
                curr_run = 1
                curr = num + 1
                while curr in vals:
                    curr_run += 1
                    curr += 1
                max_run = max(max_run, curr_run)


        return max_run