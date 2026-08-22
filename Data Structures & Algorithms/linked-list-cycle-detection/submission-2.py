# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nmb = 1
        if not head or not head.next:
            return False
        ptr1 = head
        ptr2 = head.next
        while ptr1.next and ptr2.next:
            for i in range(0,nmb):
                if not ptr2:
                    return False
                if ptr1 == ptr2:
                    return True
                ptr2 = ptr2.next
            nmb *= 2
            ptr1 = ptr2
            if ptr2:
                ptr2 = ptr2.next
            else:
                return False
        return False 