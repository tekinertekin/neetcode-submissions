# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        l = [root]
        ret = []
        while l:
            ret.append([n.val for n in l])
            l2 = []
            #print([x.val for x in l])
            for n in l:
                if n.left:
                    l2.append(n.left)
                if n.right:
                    l2.append(n.right)
            l = l2
        return ret
        