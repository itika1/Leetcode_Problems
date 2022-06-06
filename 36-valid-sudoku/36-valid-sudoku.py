class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set) # r: set("1", "2", "3", ...)
        col = collections.defaultdict(set) # c: set("1", "2", "3", ...)       
        block = collections.defaultdict(set) # (r//3, c//3): set("1", "2", "3", ...)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # don't need to check empty cells
                    continue
                # return false if the number in the cell has been filled in the same row, column, or block.
                if (board[r][c] in row[r]) or (board[r][c] in col[c]) or (board[r][c] in block[(r//3, c//3)]):
                    return False
                # otherwise, add the number to the hash set
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                block[(r//3, c//3)].add(board[r][c])
        return True
        