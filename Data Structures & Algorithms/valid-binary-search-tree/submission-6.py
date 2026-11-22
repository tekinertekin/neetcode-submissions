# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode]):
        if root.left:
            vld, lmx, lmn = self.helper(root.left)
            if not vld:
                return False, 0, 0
            if lmx >= root.val:
                return False, 0, 0
        if root.right:
            vld, rmx, rmn = self.helper(root.right)
            if not vld:
                return False, 0, 0
            if rmn <= root.val:
                return False, 0, 0
        if not root.right and not root.left:
            return True, root.val, root.val
        if root.right and root.left:
            return True, rmx, lmn
        if root.right:
            return True, rmx, root.val
        return True, root.val, lmn
        
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root)[0]
        