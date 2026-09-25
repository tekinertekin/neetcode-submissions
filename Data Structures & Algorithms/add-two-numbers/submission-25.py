# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        b = []
        while l1:
            a.append(l1)
            l1 = l1.next
        while l2:
            b.append(l2)
            l2 = l2.next
        art = 0
        new_l = []
        for i in range(0, max(len(a), len(b))):
            s = art
            if i < len(a):
                s += a[i].val
            if i < len(b):
                s += b[i].val
            new_l.append(s%10)
            art = s // 10
        if art:
            new_l.append(art)
        cpy = []
        for i in range(0, len(new_l)):
            n = ListNode(new_l[i], None)
            cpy.append(n)
        print(len(cpy))
        for i in range(0,len(cpy) - 1):
            #print(i, cpy[i].val, cpy[i+1].val)
            cpy[i].next = cpy[i+1]
        return cpy[0]
        