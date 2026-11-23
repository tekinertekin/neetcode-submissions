# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if not root:
            return 0, 0
        can_use_l, cant_use_l = self.helper(root.left)
        can_use_r, cant_use_r = self.helper(root.right)
        can_use_me = max(root.val + max(can_use_l, can_use_r), root.val)
        cant_use_me = max(root.val + can_use_l + can_use_r, cant_use_l, cant_use_r, can_use_r, can_use_l)
        return can_use_me, cant_use_me

    def return_max(self, root):
        l, r = -2000, -2000
        if root.left:
            l = self.return_max(root.left)
        if root.right:
            r = self.return_max(root.right)
        return max(r,l,root.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        use, not_use = self.helper(root)
        if max(use, not_use) <= 0:
            return self.return_max(root)
        return max(use, not_use)
        