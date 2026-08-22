# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        while head:
            next_item = head.next
            print(head.val)
            print(next_item.val if next_item else None)
            head.next = temp
            temp = head
            if next_item:
                head = next_item
            else:
                return head
        return head
        