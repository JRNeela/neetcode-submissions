# Return true if s2 contains a permutation of s1, or false otherwise. 
# That means if a permutation of s1 exists as a substring of s2, then return true.
# from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        s2_counts = defaultdict(int)
        l = 0
        r = len(s1)
        s2_counts = Counter(s2[l:r])
        while s2_counts != s1_counts and r < len(s2):
            l += 1
            r += 1
            s2_counts = Counter(s2[l:r])
        if s2_counts == s1_counts:
            return True
        else:
            return False
        


        