"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cpy = {}
        cur = head
        while cur:
            cpy[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            cpy[cur].next   = cpy.get(cur.next)
            cpy[cur].random = cpy.get(cur.random)
            cur = cur.next

        return cpy[head]