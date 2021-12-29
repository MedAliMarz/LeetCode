"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None

        
        self.connect(root.left)
        self.connect(root.right)
        
        # using other iteration variable to avoid chaning the real linking
        currLeft = root.left
        currRight = root.right
        
        # the idea is keep iterating over the right nodes under the initial left node
        # and the same for the left nodes under the initial right node
        # and change the next value for the most right nodes
        while currLeft != None:
            currLeft.next = currRight
            currLeft = currLeft.right
            currRight = currRight.left

        return root
