'''
s = "([{}])"

stack = [(, [, {]
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for letter in s:
            if letter not in hm:
                stack.append(letter)
                continue
            if not stack or stack[-1] != hm[letter]:
                return False
            stack.pop()
        if stack:
            return False
        return True  

        