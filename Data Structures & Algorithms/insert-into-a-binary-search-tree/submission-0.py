# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val<root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val>root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            pass # It is guaranteed that the new value does not exist in the original BST.
        
        return root

# locating the value in bst
# check the value against teh root node 
#     and decide to go root.right and root.left


        