class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        board_T = [[board[j][i] for j in range(n)] for i in range(n)]
        print(board_T)
        for line in board:
            dup={}
            for val in line:
                
                if val in dup:
                    print(dup)
                    return False
                elif val!=".":
                    dup[val]=1

        for line in board_T:
            dup={}
            for val in line:
                if val in dup:
                    return False
                elif val!=".":
                    dup[val]=1

        for indice__col_block in [0,3,6]:
            for indice__ligne_block in [0,3,6]:
                dup ={}
                for line_idx in range(3):
                    for column_idx in range(3):
                        val = board[indice__col_block+ line_idx][indice__ligne_block+ column_idx]
                        if val in dup:
                            return False
                        elif val!=".":
                            dup[val]=1

        return True