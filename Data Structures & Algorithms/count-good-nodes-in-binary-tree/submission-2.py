# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse_tree(self, root: TreeNode, mx):
        if not root:
            return 0
        add = 1 if mx <= root.val else 0
        if mx < root.val:
            mx = root.val
        add += self.traverse_tree(root.right, mx)
        add += self.traverse_tree(root.left, mx)
        return add
        

    def goodNodes(self, root: TreeNode) -> int:
        return self.traverse_tree(root, -200)
        