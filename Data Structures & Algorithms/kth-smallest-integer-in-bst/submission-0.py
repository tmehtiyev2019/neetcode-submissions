# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        res=[]
        curr=root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
        return res[k-1]



# #comments
# 1. extract teh BST into increaseing order list
# 2. How can we go from the minimum value to Kth minumum value?
# 3. Fiding the minimum --> go allt he way to the left
        