class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        max_count = 0
        for i in nums:
            seen.add(i)
        for i in seen:
            if i-1 not in seen:
                count = 1
                while i+count in seen:
                    count += 1
                max_count = max(count, max_count)
        return max_count





        