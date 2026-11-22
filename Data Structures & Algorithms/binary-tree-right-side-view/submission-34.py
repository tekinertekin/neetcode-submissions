# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse_tree(self, root: Optional[TreeNode], level):
        if not root:
            return
        if len(self.tree_sum) < level + 1:
            self.tree_sum.append([[root.val]])
        else:
            self.tree_sum[level].append([root.val])
        if root.left:
            self.traverse_tree(root.left, level + 1)
        if root.right:
            self.traverse_tree(root.right, level + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        self.tree_sum = []
        self.traverse_tree(root, 0)
        print(self.tree_sum)
        for it in self.tree_sum:
            ret.append(it[-1][0])
        return ret

        