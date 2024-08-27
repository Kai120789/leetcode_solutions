class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def Create(board):
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
            return columns, nines
        print(board)


        def Fill(board, columns, nines):
            for i in range(0, 9):
                for j in range(0, 9):
                    if i < 3 and j < 3:
                        if board[i][j] == '.' or len(board[i][j]) != 1:
                            board[i][j] = ''
                            for z in range(1, 10):
                                if str(z) not in board[i] and str(z) not in columns[j] and str(z) not in nines[0]:
                                    board[i][j] += str(z)
                    elif i < 3 and j < 6:
                        if board[i][j] == '.' or len(board[i][j]) != 1:
                            board[i][j] = ''
                            for z in range(1, 10):
                                if str(z) not in board[i] and str(z) not in columns[j] and str(z) not in nines[1]:
                                    board[i][j] += str(z)
                    elif i < 3 and j < 9:
                        if board[i][j] == '.' or len(board[i][j]) != 1:
                            board[i][j] = ''
                            for z in range(1, 10):
                                if str(z) not in board[i] and str(z) not in columns[j] and str(z) not in nines[2]:
                                    board[i][j] += str(z)
                    elif i < 6 and j < 3:
                        if board[i][j] == '.' or len(board[i][j]) != 1:
                            board[i][j] = ''
                            for z in range(1, 10):
                                if str(z) not in board[i] and str(z) not in columns[j] and str(z) not in nines[3]:
                                    board[i][j] += str(z)
                    elif i < 6 and j < 6:
                        if board[i][j] == '.' or len(board[i][j]) != 1:
                            board[i][j] = ''
                            for z in range(1, 10):
                                if str(z) not in board[i] and str(z) not in columns[j] and str(z) not in nines[4]:
                                    board[i][j] += str(z)
                    elif i < 6 and j < 9:
                        if board[i][j] == '.' or len(board[i][j]) != 1:
                            board[i][j] = ''
                            for z in range(1, 10):
                                if str(z) not in board[i] and str(z) not in columns[j] and str(z) not in nines[5]:
                                    board[i][j] += str(z)
                    elif i < 9 and j < 3:
                        if board[i][j] == '.' or len(board[i][j]) != 1:
                            board[i][j] = ''
                            for z in range(1, 10):
                                if str(z) not in board[i] and str(z) not in columns[j] and str(z) not in nines[6]:
                                    board[i][j] += str(z)
                    elif i < 9 and j < 6:
                        if board[i][j] == '.' or len(board[i][j]) != 1:
                            board[i][j] = ''
                            for z in range(1, 10):
                                if str(z) not in board[i] and str(z) not in columns[j] and str(z) not in nines[7]:
                                    board[i][j] += str(z)
                    else:
                        if board[i][j] == '.' or len(board[i][j]) != 1:
                            board[i][j] = ''
                            for z in range(1, 10):
                                if str(z) not in board[i] and str(z) not in columns[j] and str(z) not in nines[8]:
                                    board[i][j] += str(z)
            return board


        def Solve(board):
            flag = False
            count = 0
            while not flag:
                flag = True
                board2 = list(map(list, board))

                cnt = 0
                while cnt < 9:
                    for j in range(0, 9):
                        if len(board2[cnt][j]) != 1:
                            board2[cnt][j] = board2[cnt][j][count]
                            cnt = 9
                            break
                    cnt += 1

                columns, nines = Create(board)
                for z in range(0, 10):
                    board2 = Fill(board2, columns, nines)
                    columns, nines = Create(board2)

                for i in range(0, 9):
                    for j in range(0, 9):
                        if board2[i][j] == '':
                            flag = False

                if flag:
                    i = 0
                    while i < 9:
                        for j in range(0, 9):
                            if len(board[i][j]) != 1:
                                flag = False
                                count = -1
                                board = board2
                                i = 9
                                break
                        i += 1

                print("\n")
                for i in range(0, 9):
                    print(board2[i], "\n")

                count += 1
            return board2

    
        def Solve_2(board):
            flag = False
            count = 0

            while not flag:
                flag = True
                board2 = list(map(list, board))

                cnt = 8
                while cnt > -1:
                    for j in range(7, -1, -1):
                        if len(board2[cnt][j]) != 1:
                            board2[cnt][j] = board2[cnt][j][count]
                            cnt = 0
                            break
                    cnt -= 1

                columns, nines = Create(board)
                for z in range(0, 10):
                    board2 = Fill(board2, columns, nines)
                    columns, nines = Create(board2)

                i = 0

                while i < 9:
                    for j in range(0, 9):
                        if board2[i][j] == '':
                            flag = False
                            i = 9
                            break
                    i += 1



                if flag:
                    i = 0
                    while i < 9:
                        for j in range(0, 9):
                            if len(board[i][j]) != 1:
                                flag = False
                                count = -1
                                board = board2
                                i = 9
                                break
                        i += 1

                print("\n")
                for i in range(0, 9):
                    print(board2[i], "\n")

                count += 1
            return board2

        columns, nines = Create(board)

        for z in range(0, 10):
            board = Fill(board, columns, nines)
            columns, nines = Create(board)

        for i in range(0, 9):
            print(board[i], "\n")

        board2 = []
        i = 0
        while i < 9:
            for j in range(0, 9):
                if board[i][j] == '' or len(board[i][j]) != 1:
                    try:
                        board2 = Solve(board)
                    except IndexError:
                        board2 = Solve_2(board)
                    i = 9
                    break
            i += 1
        if board2:
            for i in range(0, 9):
                board.pop(0)
                board.append(board2[i])

        for i in range(0, 9):
            print(board[i], "\n")

        print(board2)

        return