# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
   # Handle the base case    
        if not root:
            return None
   
   # Find the node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else: # it has boh children
                MinNode = self.FindMinVal(root.right)
                root.val = MinNode.val
                root.right = self.deleteNode(root.right, MinNode.val)
        return root

    def FindMinVal(self, root):
        curr=root
        while curr and curr.left:
            curr=curr.left
        return curr

        

        

#comments









# 1. Find the node
# 2. Check their children
#     if right children is missing return left
#     elif left children is missing return rih children
#     else:
#         fin dteh MinVal val in the root.right
#         root.val = minVal
#         root.right=remove(root.right, MinVal)
# 3. To find the minimum node in the right sub-tree
