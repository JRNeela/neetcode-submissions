class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        AAABABB
         maxFreq --> A
         current_char length
         window length - maxFreq count - k <= 0
         > 0
         ->
         incremnet our left pointer
         adjust dictionary as necessary
        {
            A: 1
            
        }


        Find the most frequently occurring letter
        label that keyChar
        iterate through the list of s 
        if I find a letter that is not keyChar
        len(s) - len(keyChar) - count of current letter < 0:
            move my left pointer
            update dictionary as follows
            move on 

        '''
        from collections import Counter
        counts = {}
        right = 0
        left = 0
        maxFreq = 0
        while right < len(s):
            curr_val = s[right]
            if curr_val in counts:
                counts[curr_val] += 1
            else:
                counts[curr_val] = 1
            maxFreq = max(maxFreq, counts[curr_val])
                #Condition to check
            if (right - left + 1) - maxFreq - k > 0:
                counts[s[left]] -= 1
                left += 1
            right += 1
        return len(s) - left


        