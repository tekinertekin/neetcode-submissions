# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_item = None
        while head:
            next_item = head.next
            head.next = prev_item
            prev_item = head
            if next_item:
                head = next_item
            else:
                return head
        