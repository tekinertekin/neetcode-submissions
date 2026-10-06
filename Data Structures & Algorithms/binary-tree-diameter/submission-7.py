# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if not root:
            return -1, -1
        # 1 beni kesmeyen(bende biten), 2 kesen
        l1, l2 = self.helper(root.left)
        r1, r2 = self.helper(root.right)
        return max(r1, l1) + 1, max(l2,r2,l1+r1+2)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root))
        