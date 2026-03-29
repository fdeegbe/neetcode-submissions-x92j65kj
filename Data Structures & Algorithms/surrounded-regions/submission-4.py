class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dfs on inner cells. use a inner visited set.
        inner_visited = set()
        def dfs(row, col):
            res = False
            if (row, col) in inner_visited:
                return False
            if row in range(len(board)) and col in range(len(board[0])):
                if row in [0, len(board)-1] or col in [0, len(board[0])-1]: # if we are on the border
                    if board[row][col] == 'O':
                        print(row,col, board[row][col])
                        return True
                    else:
                        return False
                elif board[row][col] == 'O':
                    inner_visited.add((row,col))
                    res |= dfs(row+1,col)
                    res |= dfs(row-1,col)
                    res |= dfs(row,col+1)
                    res |= dfs(row,col-1)
                    return res
                else:
                    return False
            return res
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(i,j)
                if board[i][j] == 'O':
                    if not dfs(i,j):
                        print("Changing: ", inner_visited)
                        for (row,col) in inner_visited:
                            board[row][col] = 'X'
                    else:
                        print("Keeping: ", inner_visited)
                    inner_visited = set()
        