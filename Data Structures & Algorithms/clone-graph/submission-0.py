from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        root_clone = Node(node.val)
        clone_map = {node: root_clone}
        q = deque([node])        

        while q:
            curr = q.popleft()
            curr_clone = clone_map[curr]
            for nei in curr.neighbors:
                if nei not in clone_map:
                    nei_clone = Node(nei.val)
                    clone_map[nei] = nei_clone
                    q.append(nei)
                else:
                    nei_clone = clone_map[nei]
                curr_clone.neighbors.append(nei_clone)

        return root_clone