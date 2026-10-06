# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if not root:
            return 0, True
        h_l, c_l = self.helper(root.left)
        h_r, c_r = self.helper(root.right)
        return max(h_l, h_r) + 1, c_l and c_r and abs(h_l - h_r) <= 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[1]
        