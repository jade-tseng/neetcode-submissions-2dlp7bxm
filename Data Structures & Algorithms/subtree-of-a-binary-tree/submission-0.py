# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False           # ran out of tree without finding it
        if self.sameTree(root, subRoot):
            return True            # match at this node
        # otherwise, try the left subtree, then the right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def sameTree(self, a, b):
        # Both None → True (matched all the way down)
        # One None, other not → False (structure differs)
        # Values differ → False
        # Otherwise recurse: left children match AND right children match
        if not a and not b:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        else:
            return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)