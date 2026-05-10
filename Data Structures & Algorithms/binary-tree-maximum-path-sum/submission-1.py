# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            left = dfs(root.left)
            left = max(left, 0)
            right = dfs(root.right)
            right = max(right, 0)
            max_sum = max(root.val + left + right, max_sum)
            return root.val + max(left, right)
        dfs(root)
        return max_sum

        

        