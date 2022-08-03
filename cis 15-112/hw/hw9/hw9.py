#################################################
# hw9.py: Tetris!
#
# Your name:
# Your andrew id:
#
# Your partner's name:
# Your partner's andrew id:
#################################################

from queue import Empty
from socket import ntohl
import cs112_n22_week4_linter
import math, copy, random

from cmu_112_graphics import *

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def getCellBounds(app, row, col):
    x0 = app.margin + app.cellSize * col
    y0 = app.margin + app.cellSize * row
    x1 = app.margin + app.cellSize * (col + 1)
    y1 = app.margin + app.cellSize * (row + 1)

    return x0, y0, x1, y1

#################################################
# Functions for you to write
#################################################

#change dimensions here for the game
def gameDimensions():
    rows = 15
    cols = 10
    cellSize = 20
    margin = 25
    return (rows, cols, cellSize, margin)

def playTetris():
    rows, cols, cellSize, margin = gameDimensions()
    width = (cols * cellSize) + (2 * margin)
    height = (rows * cellSize) + (2 * margin)
    runApp(width=width, height=height)

def appStarted(app):

    #Game Dimenstions/Settings
    app.rows, app.cols, app.cellSize, app.margin = gameDimensions()
    app.isPaused = False
    app.isGameOver = False
    app.score = 0
    
    # Board
    app.emptyColor = "blue"
    app.board = [[app.emptyColor] * app.cols for i in range(app.rows)]

    # Tetris piecies
    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]

    app.tetrisPieces = [ iPiece, jPiece, lPiece, 
                         oPiece, sPiece, tPiece, 
                         zPiece ]
    app.tetrisPieceColors = [ "red", "yellow", "magenta",
                              "pink", "cyan", "green", 
                              "orange" ]
    app.fallingPiece = None
    app.fallingPieceColor = None
    app.fallingPieceRow = None
    app.fallingPieceCol = None
    newFallingPiece(app)


def keyPressed(app, event):
    if not app.isGameOver:
        if event.key == "Right":
            moveFallingPiece(app, 0, 1)
        elif event.key == "Left":
            moveFallingPiece(app, 0, -1)
        elif event.key == "Down":
            moveFallingPiece(app, +1, 0)
        elif event.key == "Up":
            rotatingFallingPiece(app)
        elif event.key == "Space":
            while moveFallingPiece(app, +1, 0):
                pass
        elif event.key == "p":
            app.isPaused = not app.isPaused
        elif event.key == "s":
            doStep(app)
    if event.key == "r":
            appStarted(app)
    
def timerFired(app):
    if not app.isGameOver and not app.isPaused:
        doStep(app)

def doStep(app):
    if not moveFallingPiece(app, 1, 0) and fallingPieceIsLegal(app):
            placeFallingPiece(app)
            newFallingPiece(app)
            if not fallingPieceIsLegal(app) and not app.isPaused:
                app.isGameOver = True

# Falling Piece

def newFallingPiece(app):
    randomIndex = random.randint(0, len(app.tetrisPieces) - 1)
    randomIndex2 = random.randint(0, len(app.tetrisPieceColors) - 1)
    app.fallingPiece = app.tetrisPieces[randomIndex]
    app.fallingPieceColor = app.tetrisPieceColors[randomIndex2]
    numFallingPieceRows = len(app.fallingPiece)
    numFallingPieceCols = len(app.fallingPiece[0])

    app.fallingPieceRow = 0 
    app.fallingPieceCol = app.cols//2 - numFallingPieceCols//2

def moveFallingPiece(app, drow, dcol):
    app.fallingPieceRow += drow
    app.fallingPieceCol += dcol

    if not fallingPieceIsLegal(app):
        app.fallingPieceRow -= drow
        app.fallingPieceCol -= dcol
        return False
    return True

def rotatingFallingPiece(app):
    temp = copy.deepcopy(app.fallingPiece)
    rows = len(app.fallingPiece[0])

    cols = len(app.fallingPiece)
    newFallingPiece = [[False] * cols for i in range(rows)]
    for row in range(len(app.fallingPiece)):
        for col in range(len(app.fallingPiece[0])):
            moveValue = app.fallingPiece[row][col]
            newFallingPiece[len(app.fallingPiece[0])-1-col][row] = moveValue

    app.fallingPiece = copy.deepcopy(newFallingPiece)

    tempRow, tempCol = app.fallingPieceRow, app.fallingPieceCol
    app.fallingPieceRow = (app.fallingPieceRow + len(temp)//2 
                        - len(app.fallingPiece)//2)
    app.fallingPieceCol = (app.fallingPieceCol + len(temp[0])//2 
                        - len(app.fallingPiece[0])//2)

    if not fallingPieceIsLegal(app):
        print('invalid')
        app.fallingPiece = temp
        app.fallingPieceRow, app.fallingPieceCol = tempRow, tempCol

def fallingPieceIsLegal(app):
    for row in range(len(app.fallingPiece)):
        for col in range(len(app.fallingPiece[0])):
            currentRow = row + app.fallingPieceRow
            currentCol = col + app.fallingPieceCol
            # check if its outside boundary
            if (currentRow not in range(len(app.board)) 
               or currentCol not in range(len(app.board[0]))):
                return False
            elif ((app.board[currentRow][currentCol] != app.emptyColor)
                   and app.fallingPiece[row][col] == True):
                #if block collides return False
                return False
    return True

def placeFallingPiece(app):
    for row in range(len(app.fallingPiece)):
        for col in range(len(app.fallingPiece[0])):
            if app.fallingPiece[row][col]:
                boardRow = row + app.fallingPieceRow
                boardCol = col + app.fallingPieceCol
                app.board[boardRow][boardCol] = app.fallingPieceColor
    removeFullRows(app)

def removeFullRows(app):
    total = 0
    for row in range(len(app.board)):
        count = 0
        for col in range(len(app.board[0])):
            if app.board[row][col] != app.emptyColor:
                count += 1
        if count == app.cols:
            app.board.pop(row)
            app.board.insert(0, [app.emptyColor] * app.cols)
            total += 1

    if total > 0:
        app.score += total ** 2


#################################################
# View
#################################################

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "orange")
    drawBoard(app, canvas)
    if app.fallingPiece:
        drawFallingPiece(app, canvas)
    if app.isGameOver:
        drawGameOver(app, canvas)
    drawScore(app, canvas)

def drawCell(app, canvas, row, col, color):
    x0, y0, x1, y1 = getCellBounds(app, row, col)
    canvas.create_rectangle(x0, y0, x1, y1, 
                            fill = color, 
                            width = 2, outline = "black")

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, canvas, row, col, app.board[row][col])


def drawFallingPiece(app, canvas):
    for row in range(len(app.fallingPiece)):
        for col in range(len(app.fallingPiece[0])):
            if app.fallingPiece[row][col]:
                drawCell(app, canvas, row + app.fallingPieceRow, 
                                      col + app.fallingPieceCol, 
                                      app.fallingPieceColor)

def drawScore(app, canvas):
    canvas.create_text(app.width/2, 12, text = f"Score: {app.score}", 
                       font = "Times 20 bold", fill = "purple")

def drawGameOver(app, canvas):
    x0,y0 = getCellBounds(app,1,0)[0:2]
    x1,y1 = getCellBounds(app, 3, app.cols-1)[2:4]
    canvas.create_rectangle(x0,y0,x1,y1, fill = "black")
    canvas.create_text((x0+x1)/2,(y1+y0)/2, text="Game Over", 
                            fill="yellow", font="Times 35 bold")

#################################################
# main
#################################################

def main():
    cs112_n22_week4_linter.lint()
    playTetris()

if __name__ == '__main__':
    main()
