class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nb_row, nb_col = 9, 9

        # space O(n*n)
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [[set() for _ in range(3)] for _ in range(3)]

        # time O(81) or time O(n*n)
        for i in range(nb_row):
            for j in range(nb_col):
                val = board[i][j]
                if val == ".":
                    continue
                if val in row[i] or val in col[j] or val in block[i//3][j//3]:
                    return False
                else:
                    row[i].add(val)
                    col[j].add(val)
                    block[i//3][j//3].add(val)
        
        return True