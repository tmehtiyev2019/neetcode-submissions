# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         out=[]
#         def inorder(node):
#             if not node:
#                 return
#             inorder(node.left)
#             out.append(node.val)
#             inorder(node.right)
#         inorder(root)
#         return out



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res



# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         stack = []
#         cur = root

#         while cur or stack:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             res.append(cur.val)
#             cur = cur.right

#         return res
            
