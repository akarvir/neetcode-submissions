# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = ""
        def dfs(r):
            nonlocal s
            if not r:
                s += "N"
                s+="#"
            else:
                s+=str(r.val)
                s+="#"
                dfs(r.left)
                dfs(r.right)
        dfs(root)
        return s
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = -1
        def dfs():
            nonlocal i
            i+=1
            node = None
            if data[i] != "N":
                num = ""
                while data[i]!="#":
                    num = num + data[i]
                    i+=1
                num = int(num)
                node = TreeNode(num,None,None)
                node.left = dfs()
                node.right = dfs()
            else:
                i+=1
            return node

        return dfs()

