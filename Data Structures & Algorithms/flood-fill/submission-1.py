class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        stack = [(sr, sc)]
        start_color = image[sr][sc]
        image[sr][sc] = color
        if start_color == color:
            return image
        while stack:
            r, c = stack.pop()
            # check all directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == start_color:
                    image[nr][nc] = color
                    stack.append((nr, nc))
        return image






# directions: [(0, 1), (1, 0), (0, -1), (-1, 0)]
# same color as the starting pixel (sr, sc)
# stop when there are no more adj pixel


[[1,2,3],
[4,5,6],
[7,8,9]]
        