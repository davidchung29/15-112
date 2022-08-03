def printBoard(board):
    for row in board:
        print(row)

def knightsTourHelper(rows, cols, crow, ccol, visited, count):
    print(crow, ccol, count)
    printBoard(visited)
    possMoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]
    zeroCount = 0
    for row in visited:
        for element in row:
            if element == (rows*cols):
                return visited
    for move in possMoves:
        drow = move[0]
        dcol = move[1];
        tempRow = crow + drow
        tempCol = ccol + dcol
        if ((0 <= tempRow < rows) and (0 <= tempCol < cols)):
            if (visited[tempRow][tempCol] == 0):
                print("hi")
                count += 1
                visited[tempRow][tempCol] = count
                if knightsTourHelper(rows, cols, tempRow, tempCol, 
                                                 visited, count):
                    print("1")
                    return True
                count -= 1 
                visited[tempRow][tempCol] = 0
    return False

def knightsTour(rows, cols):
    board = [[0] * cols for _ in range(rows)]
    board[0][0] = 1
    print(knightsTourHelper(rows, cols, 0, 0, board, 1))
    return board



knightsTour(3,4)