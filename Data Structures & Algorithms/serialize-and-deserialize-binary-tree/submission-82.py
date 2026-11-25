# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize_helper(self, node):
        if not node:
            return "(N)"
        s = str(node.val)
        s += self.serialize_helper(node.left)
        s += self.serialize_helper(node.right)
        return "(" + s + ")"

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        return self.serialize_helper(root)

    def deserialize_helper(self, s):
        self.i += 1                      # "(" işaretini geç
        if s[self.i] == "N":
            self.i += 2                  # "N" ve ")" işaretlerini geç
            return None
        start = self.i
        while s[self.i] != "(":          # değerin sonuna kadar yürü
            self.i += 1
        node = TreeNode(int(s[start:self.i]))
        node.left = self.deserialize_helper(s)
        node.right = self.deserialize_helper(s)
        self.i += 1                      # bu düğümün ")" işaretini geç
        return node

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        self.i = 0
        return self.deserialize_helper(data)
