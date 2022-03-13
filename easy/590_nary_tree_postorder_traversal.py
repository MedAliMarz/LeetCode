"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if root == None:
            return []
        
        array = []
        if (root.children != None):
            for child in root.children:
                array += self.postorder(child)
        array.append(root.val)
        
        return array
