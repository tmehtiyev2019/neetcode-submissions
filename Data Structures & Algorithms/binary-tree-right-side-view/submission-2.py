# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        q = deque([(root, 1)])
        res = []

    
        while q:
            node, level = q.popleft()
            if len(res) < level:
                res.append(node.val)

            if node.right:
                q.append((node.right, level + 1))

            if node.left:
                q.append((node.left, level + 1))
        return res



# Input: root = [1,2,3,null,4,null,5]

# Output: [1,3,5]
        