'''
Goal: Generate all possible pairs of parentheses strings with n pairs

Break down the problem:
    how do I ensure that I only create valid parentheses string?
    how do I generate a parentheses string using n pairs?

never start with a ), ) only follows if there was a ( present
count = 2
two instances of () --> (()), ()(), 

start with a ( --> two choices: continue with another ( or end it with )

store a record of every pair started

""

( --> ((
( --> ()

params -> total number of completed parenthesis, parentheseses in progress

if completed parentheses + paren in progress < k --> add a (
if parentheses in progress --> add a )
if both --> do both
if neither --> add string and return

psuedo
dfs according to the above, keeping trak of both params
return ret

'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def dfs(curr, numInProgress, numCompleted):
            if numCompleted == n and numInProgress == 0:
                ret.append(curr[:])
                return  # Add return to avoid over-recursing
            if numInProgress > 0:
                dfs(curr + ")", numInProgress - 1, numCompleted + 1)
            if numCompleted + numInProgress < n:
                dfs(curr + "(", numInProgress + 1, numCompleted)
        
        dfs("", 0, 0)
        return ret


        