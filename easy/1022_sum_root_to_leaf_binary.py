# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        arr = []
        return self.sum_root_to_leaf( root, arr)

    def sum_root_to_leaf(self, root, arr) -> int:

        if root == None:
            return 0
        
        arr.append(str(root.val))
        result = 0

        if root.left == None and root.right == None:
            result =  int(''.join(arr), 2)
        else:
            result = self.sum_root_to_leaf(root.left, arr) + self.sum_root_to_leaf(root.right, arr)
        
        arr.pop()    
        return result
            
