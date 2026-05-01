# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0                    # base case: empty tree, height 0

            left = height(node.left)
            if left == -1:                  # ② CHECK: did the left subtree signal unbalanced?
                return -1                   # ③ PROPAGATE: pass the signal up to my parent

            right = height(node.right)
            if right == -1:                 # ② CHECK: did the right subtree signal unbalanced?
                return -1                   # ③ PROPAGATE

            if abs(left - right) > 1:       # ① DETECT: imbalance found at this node
                return -1                   # ① SIGNAL: emit the sentinel

            return 1 + max(left, right)     # normal case: return real height

        return height(root) != -1           # ④ INTERPRET: convert sentinel-or-height into bool
