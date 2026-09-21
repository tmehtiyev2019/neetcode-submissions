# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 1
        q = deque([(root,level)])

        while q:
            curr_node, curr_level = q.popleft()
            if curr_node.right:
                q.append((curr_node.right, curr_level+1))
            if curr_node.left:
                q.append((curr_node.left, curr_level+1))
        return curr_level




# 1. we start with the root node:
# 2. We have a queue with the root node (we also store the level togtehr with the node)
# 3. We do BFS and everytime add 1 to the lvel variable
# 4. Int he end we check if right and left is null meaning that we cannot go any further
# 5. We return the level


# Question:
# q: how do we know that the lvel we return is the max depth?
# a: since we are doing bfs, the last node will be in the final layer of BT
        
# Edge cases:

# 1. onyl one node--> return 1
# 2. empty (meaning node is none) --> return 0