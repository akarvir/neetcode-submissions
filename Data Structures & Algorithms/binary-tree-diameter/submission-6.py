# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxval = 0

        def height(r):
            nonlocal maxval
            if not r:
                return 0
            left = height(r.left)
            right = height(r.right)
            maxval = max(left+right,maxval)
            return 1 + max(left,right)
        height(root)
        return maxval
            
