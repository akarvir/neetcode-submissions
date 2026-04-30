# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# a path it can actually follow, either the left or the right.
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def dfs(v):
            nonlocal ans
            if not v:
                return 0
            left = max(dfs(v.left),0)
            right = max(dfs(v.right),0)
            ans = max(ans,v.val + left + right)
            return v.val + max(left,right)
        dfs(root)
        return ans