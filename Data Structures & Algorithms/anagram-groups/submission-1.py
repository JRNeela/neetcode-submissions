'''
to check if two strings are anagrams --> O(n*m) space with hashmap

aim for O(m) space where m is the number of strings

O(n*m) complexity --> iterate through every character

we can compare hashmaps for each str

we have a list of possible char frequencies

for each frequency, 
'''
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_freqs = defaultdict(list)
        ret = []
        for s in strs:
            sorted_word = "".join(sorted(s))
            list_of_freqs[sorted_word].append(s)
        for freq_map, val in list_of_freqs.items():
            ret.append(val)
        return ret

            



        