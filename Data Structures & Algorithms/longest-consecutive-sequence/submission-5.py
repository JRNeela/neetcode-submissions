'''
O(n) time

elements do not need to be consecutive in og array

make a set of seen numbers; if num is not seen, this is a start

while i+1 in set, we append to curr_max then finish by adding num t oet
'''
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        abs_max = 0
        for num in nums:
            seen.add(num)
        for num in nums:
            curr_max = 0
            curr = num
            while curr in seen:
                curr_max += 1
                curr -= 1
            abs_max = max(abs_max, curr_max)


        return abs_max




        