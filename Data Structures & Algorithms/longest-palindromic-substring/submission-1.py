'''
return longest palindrome substring

dp[n] --> length longest palindrome

0 --> n

j < i

"ababd"

if s[i] == s[j] --> dp[i] = j - i + 1, 
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        n = len(s)
        def expand(i, j):
            l = i
            r = j
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]
        #find palindrome assuming each index is the middle
        #we can have odd or even palindromes
        for i in range(n):
            odd = expand(i,i)
            even = expand(i, i+1)
            if len(odd) > len(ret):
                ret = odd
            if len(even) > len(ret):
                ret = even
        return ret


        