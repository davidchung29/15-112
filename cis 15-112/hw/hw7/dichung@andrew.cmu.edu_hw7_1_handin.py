#################################################
# hw7: One-Dimensional Connect Four
# name:
# andrew id:
# 
#################################################

from sys import builtin_module_names
import cs112_n22_week3_linter
from cmu_112_graphics import *
import random, string, math, time

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def getCellBounds(app, piece):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    cellWidth = app.width / app.boardCount
    x0 = piece * cellWidth
    x1 = (piece+1) * cellWidth
    y0 = (app.height/2) - cellWidth/2
    y1 = (app.height/2) + cellWidth/2
    return (x0, y0, x1, y1)

def getPieceXY(app, x, y):
    cellWidth = app.width/app.boardCount
    index = x/cellWidth
    if y > (app.height/2 - cellWidth/2) and y < (app.height/2 + cellWidth/2):
        return int(index//1)

def getPieceCenter(app, pieceIndex):
    x0, y0 = getCellBounds(app, pieceIndex)[0:2]
    return x0 + app.radius, y0 + app.radius

def verifySelection(app, piece):
    if piece != 0 and piece != app.boardCount - 1:
        if app.playerBlue:
            if "blue" in app.board[piece-1:piece+2]:
                return True
            else:
                app.message = 'Block must contain current player'
        else:
            if "green" in app.board[piece-1:piece+2]:
                return True
            else:
                app.message = 'Block must contain current player'
    else:
        app.message = 'End cannot be in block'
    
def verifyMove(app, piece):
    if (piece == 0) or (piece == app.boardCount - 1):
        return True

#################################################
# main app
#################################################

def appStarted(app):
    app.boardCount = 6
    app.board = []
    app.margin = 5
    app.border = 7
    refreshBoard(app)

    app.selection = None
    app.playerBlue = True
    app.message = "Select your 3-piece block"
    app.winner = None
    app.winIndex = None # last index for win sequence

    app.isGameOver = False

def refreshBoard(app):
    app.board = []
    app.radius = (app.width/app.boardCount)/2 - app.margin
    randomColor = random.randint(0,2)
    for x in range(app.boardCount):
        if x%2 == 0:
            app.board.append("blue")
        else:
            app.board.append("green")
    if randomColor:
        app.board = app.board[::-1]

def moveSelection(app, piece):
    temp = app.board[app.selection-1:app.selection+2]
    remainder = app.board[0:app.selection-1] + app.board[app.selection+2:]
    app.selection = None
    if piece == 0:
        app.board = temp + remainder
    else:
        app.board = remainder + temp

def mousePressed(app, event):
    print(app.isGameOver, checkWin(app))
    if not app.isGameOver:
        piece = getPieceXY(app, event.x, event.y)
        if piece != None:
            if verifySelection(app, piece):
                app.selection = piece
                app.message = 'Select end to move block to'
            elif verifyMove(app, piece) and app.selection != None:
                moveSelection(app, piece)
                if not checkWin(app):
                    app.playerBlue = not app.playerBlue
                    app.message = 'Select your 3-piece block'
        else:
            app.move = None

def checkWin(app):
    seq = []
    for i in range(len(app.board)):
        print(app.board[i], seq)
        if app.board[i] in seq:
            seq.append(app.board[i])
        if len(seq) >= 4:
            if (app.playerBlue == (seq[0] == "blue")): 
                print('won wonw onw')
                app.winner = seq[0]
                app.winIndex = i - len(seq) + 1
                app.message = 'Game Over!!!!!'
                app.isGameOver = True
                return True
                break
        if app.board[i] not in seq:
            seq = [app.board[i]]
        

def keyPressed(app, event):
    if event.key == "Up" and app.boardCount < 20:
        app.boardCount += 2
        refreshBoard(app)
    elif event.key == "Down" and app.boardCount > 6:
        app.boardCount -= 2
        refreshBoard(app)
    elif event.key == "c":
        if app.selection:
            if app.playerBlue:
                color = "blue"
            else:
                color = "green"
            app.board[app.selection - 1] = color
            app.board[app.selection] = color
            app.board[app.selection + 1] = color
    elif event.key == "p":
        app.playerBlue = not app.playerBlue  
    elif event.key == "r":
        appStarted(app)


def redrawAll(app, canvas):
    if app.selection:
        drawSelection(app,canvas)
    drawTitle(app, canvas)
    drawInstructions(app, canvas)
    drawCurrentPlayerAndMessage(app, canvas)
    drawBoard(app, canvas)
    drawRules(app, canvas)
    if app.winner:
        drawWinLine(app, canvas)

def drawTitle(app, canvas):
    canvas.create_text((app.width/2, 20), 
                        text = "One-Dimensional Connect Four!", )

def drawInstructions(app, canvas):
    messages = ['See rules below.',
                'Click interior piece to select center of 3-piece block.',
                'Click end piece to move that block to that end.',
                'Change board size (and then restart) with arrow keys.',
                'For debugging, press c to set the color of selected block.',
                'For debugging, press p to change the current player.',
                'Press r to restart.',
               ]
    for x in range(len(messages)):
        canvas.create_text((app.width/2, (x+2) * 20), text = messages[x])

def drawRules(app, canvas):
    messages = [
  "The Rules of One-Dimensional Connect Four:",
  "Arrange N (10 by default) pieces in a row of alternating colors.",
  "Players take turns to move three pieces at a time, where:",
  "      The pieces must be in the interior (not on either end)",
  "      The pieces must be adjacent (next to each other).",
  "      At least one moved piece must be the player's color.",
  "The three pieces must be moved in the same order to either end of the row.",
  "The gap must be closed by sliding the remaining pieces together.",
  "The first player to get four (or more) adjacent pieces of their color wins!",
               ]
    for x in range(len(messages)):
        canvas.create_text((app.width/2, app.height - (x + 2) * 20),
                            text = messages[x])

def drawCurrentPlayerAndMessage(app, canvas):
    if app.playerBlue:
        color = "blue"
    else:
        color = "green"
    canvas.create_text(300, 190, text = "Current Player", fill = color)
    canvas.create_oval(350, 170, 380, 200, fill = color)
    canvas.create_text(500, 190, text = app.message, fill = color)

def drawSelection(app, canvas):
    for selection in range(app.selection-1, app.selection+2):
        (x0, y0, x1, y1) = getCellBounds(app, selection)
        canvas.create_rectangle(x0, y0, x1, y1, fill = "orange")


def drawPlayerPiece(app, canvas, player, cx, cy):
    canvas.create_oval(cx - app.radius, cy - app.radius,
                           cx + app.radius, cy + app.radius,
                           fill = app.board[player])
        # create overlay lighter circle
    canvas.create_oval(cx - app.radius + app.border, 
                       cy - app.radius + app.border,
                       cx + app.radius - app.border, 
                       cy + app.radius - app.border,
                       fill = "light" + str(app.board[player]))

def drawBoard(app, canvas):
    for piece in range(app.boardCount):
        # draw grid
        (x0, y0, x1, y1) = getCellBounds(app, piece)
        canvas.create_rectangle(x0, y0, x1, y1, outline = "white")
        #draw circles
        # add radius bc this is circles center
        cx, cy = x0 + app.margin + app.radius, y0 + app.margin + app.radius
        drawPlayerPiece(app, canvas, piece, cx, cy)

def drawWinLine(app, canvas):
    x0,y0 = getPieceCenter(app, app.winIndex)
    x1, y1 = getPieceCenter(app, app.winIndex+3)
    canvas.create_line(x0,y0,x1,y1)


def main():
    cs112_n22_week3_linter.lint()
    runApp(width=800, height=550)

if __name__ == '__main__':
    main()