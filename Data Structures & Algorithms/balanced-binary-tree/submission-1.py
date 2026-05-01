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
                return 0, True

            left, left_truth = height(node.left)
            right, right_truth = height(node.right)

            if abs(left - right) > 1 or not left_truth or not right_truth:
                return -1, False

            return 1 + max(left, right), True

        return height(root)[1]

        