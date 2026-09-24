# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_dict = defaultdict(list)
        q = deque()
        res = []
        q.append((root, 0))
        while q:
            curr, level = q.popleft()
            level_dict[level].append(curr.val)
            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:  
                q.append((curr.right, level + 1))
        for val in level_dict.values():
            res.append(val)
        return res


#complexity:
# time: O(n)
# space: O(n)
# edge cases:

# the tree is empty:
# level_dict = {
#     0: [1]
#     1: [2,3]
#     3: [4, 5, 6, 7]
# }


[1]
[2,3]
        