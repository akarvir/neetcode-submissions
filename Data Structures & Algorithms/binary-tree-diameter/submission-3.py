# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# any diameter is in fact the height of a small enough binary tree. we look at all trees, so we catch, dont worry. 
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def height(r):
            if not r:
                return 0
            return 1 + max(height(r.left),height(r.right))
        return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right),height(root.left)+height(root.right))

        