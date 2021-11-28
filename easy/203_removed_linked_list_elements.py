# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        else:
            if head.val == val:
                head =  self.removeElements(head.next, val)
            else:
                head.next = self.removeElements(head.next, val)
            return head



