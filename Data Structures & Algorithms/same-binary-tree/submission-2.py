# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # check the edge cases
#         if not q and not p:
#             return True
#         if not q or not p:
#             return False

#         que_1 = deque([q])
#         que_2 = deque([p])

#         while que_1 and que_2:
#             curr_1 = que_1.popleft()
#             curr_2 = que_2.popleft()
#             if curr_1.val != curr_2.val:
#                 return False

#             if curr_1.left and curr_2.left:
#                 que_1.append(curr_1.left)
#                 que_2.append(curr_2.left)
#             elif curr_1.left or curr_2.left:
#                 return False

#             if curr_1.right and curr_2.right:
#                 que_1.append(curr_1.right)
#                 que_2.append(curr_2.right)
#             elif curr_1.right or curr_2.right:
#                 return False
    

#         if que_1 or que_2:
#             return False
#         return True





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check the edge cases
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

       