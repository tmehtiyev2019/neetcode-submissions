
# Iterative DFS
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         ROWS, COLS = len(image), len(image[0])
#         stack = [(sr, sc)]
#         start_color = image[sr][sc]
#         image[sr][sc] = color
#         if start_color == color:
#             return image
#         while stack:
#             r, c = stack.pop()
#             # check all directions
#             for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                 nr = r + dr
#                 nc = c + dc
#                 if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == start_color:
#                     image[nr][nc] = color
#                     stack.append((nr, nc))
#         return image

# BFS
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         ROWS, COLS = len(image), len(image[0])
#         queue = deque()
#         queue.append((sr, sc))
#         start_color = image[sr][sc]
#         image[sr][sc] = color
#         if start_color == color:
#             return image
#         while queue:
#             r, c = queue.popleft()
#             # check all directions
#             for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                 nr = r + dr
#                 nc = c + dc
#                 if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == start_color:
#                     image[nr][nc] = color
#                     queue.append((nr, nc))
#         return image



# Recursive DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        start_color = image[sr][sc]
        #no work is needed
        if start_color == color:
            return image

        def dfs(r, c):

            if not 0 <= r < ROWS or not 0 <= c < COLS or image[r][c] != start_color:
                return
            else:
                image[r][c] = color
            # check all directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)

        dfs(sr, sc)
        return image

        


# in Recursion:
# we need to define teh base case





# directions: [(0, 1), (1, 0), (0, -1), (-1, 0)]
# same color as the starting pixel (sr, sc)
# stop when there are no more adj pixel


# [[1,2,3],
# [4,5,6],
# [7,8,9]]
        