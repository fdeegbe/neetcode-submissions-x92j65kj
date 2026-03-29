class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            m = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in m:
                    return False
                else:
                    m.add(board[i][j])

            m = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in m:
                    return False
                else:
                    m.add(board[j][i])

        # now we check individual cells
        # i = 0
        # while True:
        #     pass
        m = set()
        for row in [0, 3, 6]:
            for col in range(0,9,3):
                m = set()
                for i in range(3):
                    for j in range(3):
                        if board[j+row][i+col] != '.' and board[j+row][i+col] in m:
                            return False
                        else:
                            m.add(board[j+row][i+col])

        return True

            
        