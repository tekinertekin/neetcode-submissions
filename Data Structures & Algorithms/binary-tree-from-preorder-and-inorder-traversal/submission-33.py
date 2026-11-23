# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, start_p, end_p, start_i, end_i):
        if start_p >= end_p or start_i >= end_i:
            return None
        r = self.preorder[start_p]
        ind = self.pos[r]
        root = TreeNode(r)
        root.left = self.helper(start_p + 1, start_p + 1 + ind - start_i, start_i, ind)
        root.right = self.helper(start_p + 1 + ind - start_i, end_p, ind + 1, end_i)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        self.pos = {val: i for i, val in enumerate(inorder)}
        return self.helper(0, len(preorder), 0, len(inorder))
        