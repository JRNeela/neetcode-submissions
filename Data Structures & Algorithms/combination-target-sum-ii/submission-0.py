'''
goal: return a list of unique combinations that sum up to target

dfs

how can we ensure that there are no duplicates within the ret?

let ret be a dict: -->O(n) storage
    if the subset is already there, we can skip adding the sublist and just return

*each element needs to be at most once in a combination*
--> incoporate some sort of system that keeps track if something is used or not

if sum == target --> add list to ret and return 

dfs --> 0(n)

dfs(curr_subset, use_list, curr_idx)

how to know whether or not to append a character --> check uselist

uselist is a dictionary with either a 0 or 1 indicating whether a number has been used

if uselist[candidates[i]] == 0:
    append candidatates[i] to subset
    update uselist =
    dfs(subset, uselist, i+1)
else:
    leave everything same (do not do anything)
    dfs(subset, uselist, i+1)

iterate through candidates and dfs on each --> 0(n)
    initalize a use list for each
    run dfs()

Runtime: 0(n^2)
Space: O(n)

'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates

        def dfs(start, path, remaining):
            if remaining == 0:
                res.append(path[:])  # clone path
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicates
                if candidates[i] > remaining:
                    break  # no point in going further
                path.append(candidates[i])
                dfs(i + 1, path, remaining - candidates[i])  # i+1 to avoid reuse
                path.pop()

        dfs(0, [], target)
        return res
        



        