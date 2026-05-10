'''
to check if two strings are anagrams --> O(n*m) space with hashmap

aim for O(m) space where m is the number of strings

O(n*m) complexity --> iterate through every character




'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        ret =[]
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            hm[tuple(key)].append(s)
        for key, val in hm.items():
            ret.append(val)
        return ret
            

        