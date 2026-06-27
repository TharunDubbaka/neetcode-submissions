class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seenr=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in seenr:
                    return False
                else:
                    seenr.add(board[i][j])
        for i in range(9):
            seenc=set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                if board[j][i] in seenc:
                    return False
                else:
                    seenc.add(board[j][i])
        for sq in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row = (sq//3)*3+i
                    col = (sq%3)*3+j
                    if board[row][col]==".":
                        continue
                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        return True

