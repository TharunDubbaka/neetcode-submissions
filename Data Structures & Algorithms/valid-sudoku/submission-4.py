class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hr=collections.defaultdict(set)
        hc=collections.defaultdict(set)
        hs=collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if (board[i][j] in hr[i] or board[i][j] in hc[j] or board[i][j] in hs[(i//3,j//3)]):
                    return False
                hr[i].add(board[i][j])
                hc[j].add(board[i][j])
                hs[(i//3),(j//3)].add(board[i][j])
        return True

