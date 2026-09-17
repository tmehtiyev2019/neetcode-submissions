# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return None

        curr = root
        good_count= 1
        stack = []
 
        if curr.left:
            stack.append((curr.left,curr.val))
        if curr.right:
            stack.append((curr.right,curr.val))
        if not curr.left and not curr.right:
            return 1


        while stack:
            curr, prev_max = stack.pop()
            if curr.val >= prev_max:
                good_count += 1
            if curr.left: 
                stack.append((curr.left, max(prev_max, curr.val)))
            if curr.right:
                stack.append((curr.right, max(prev_max, curr.val)))

        return good_count

        
        