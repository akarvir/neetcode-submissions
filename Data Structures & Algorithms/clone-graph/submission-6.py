"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        def dfs(v):
            nonlocal d
            if v in d:
                return d[v]
            t = Node(v.val,[])
            d[v] = t
            for e in v.neighbors:
                t.neighbors.append(dfs(e))
            return t
        return dfs(node) if node else None

            