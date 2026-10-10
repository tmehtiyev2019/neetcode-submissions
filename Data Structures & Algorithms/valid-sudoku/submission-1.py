class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True



































        # dup_map=set()
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] in dup_map and board[i][j]!=".":
        #             print("row issue")
        #             return False
        #         dup_map.add(board[i][j])
        #     dup_map.clear()

        # for i in range(len(board[0])):
        #     for j in range(len(board)):
        #         if board[i][j] in dup_map and board[i][j]!=".":
        #             print("column issue")
        #             return False
        #         dup_map.add(board[i][j])
        #     dup_map.clear()

        # dup_map=defaultdict(set)
        # for i in range(len(board[0])):
        #     for j in range(len(board)):
        #         if board[i][j] in dup_map[(i//3,j//3)] or board[i][j] in dup_map[(i//3,j//3)]  board[i][j]!=".":
        #             print("subbox issue")
        #             return False
        #         dup_map[(i//3,j//3)].add(board[i][j])
        # return True
        

            

