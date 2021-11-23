# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head

        val = head.val
        curr = head.next
        while curr.val == val and curr.next != None:
            curr = curr.next
        
        head.next = self.deleteDuplicates( curr if curr.val != head.val else curr.next)
        return head
        


# No test because building the list is required first
