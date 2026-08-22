# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #if not head or not head.next:
        #    return None
        dummy = ListNode()
        dummy.next = head
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        it = count - n
        count = 0
        temp = dummy
        while temp:
            if count == it:
                temp.next = temp.next.next if temp.next else None
            temp = temp.next
            count += 1
        return dummy.next
        