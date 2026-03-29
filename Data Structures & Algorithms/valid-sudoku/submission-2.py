class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create some dictionaries to hold sets of which contain our dupe checking
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                # store the rows and columns in their individual sets: only requires one pass
                if board[r][c] != '.' and (board[r][c] in rows[r] or
                                            board[r][c] in cols[c] or
                                            board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])
                    
        return True
            
        