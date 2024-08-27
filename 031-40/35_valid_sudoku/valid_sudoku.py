class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if len(set(row))-1 != len(row)-row.count('.'):
                return False

        columns = []
        column = []
        count = 0
        while count < 9:
            count2 = 0
            while count2 < 9:
                column.append(str(board[count2][count]))
                if count2 == 8:
                    columns.append(column)
                    column = []
                count2 += 1

            count += 1

        for el in columns:
            if len(set(el))-1 != len(el)-el.count('.'):
                return False


        nines = [[], [], [], [], [], [], [], [], []]
        count = 0
        while count < 9:
            count2 = 0
            while count2 < 9:
                if count < 3 and count2 < 3:
                    nines[0].append(str(board[count][count2]))
                elif count < 3 and count2 < 6:
                    nines[1].append(str(board[count][count2]))
                elif count < 3 and count2 < 9:
                    nines[2].append(str(board[count][count2]))
                elif count < 6 and count2 < 3:
                    nines[3].append(str(board[count][count2]))
                elif count < 6 and count2 < 6:
                    nines[4].append(str(board[count][count2]))
                elif count < 6 and count2 < 9:
                    nines[5].append(str(board[count][count2]))
                elif count < 9 and count2 < 3:
                    nines[6].append(str(board[count][count2]))
                elif count < 9 and count2 < 6:
                    nines[7].append(str(board[count][count2]))
                else:
                    nines[8].append(str(board[count][count2]))
                count2 += 1
            count += 1
        
        for el in nines:
            if len(set(el))-1 != len(el)-el.count('.'):
                return False

        
        return True