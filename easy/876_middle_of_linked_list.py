# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterate over the linked list and get number of nodes

        curr = head
        number = 0
        while curr != None:
            number += 1
            curr = curr.next
        middle_index = number // 2

        # iterate until reaching middle and return
        index = 0
        curr = head
        while index != middle_index:
            curr = curr.next
            index += 1
        return curr
