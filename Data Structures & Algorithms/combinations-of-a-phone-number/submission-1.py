class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        hm = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        ret = []
        string = []
        numberLen = len(digits)
        def backtrack(index, string):
            if index == numberLen:
                ret.append(''.join(string))
                return
            for i in hm[digits[index]]:
                string.append(i)
                backtrack(index+1, string)
                string.pop()
        backtrack(0, string)
        return ret
        