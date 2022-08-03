#################################################
# hw5.py
#
# Your name: David Chung
# Your andrew id: dichung
# Section: A
#################################################

import cs112_n22_week2_linter
from cmu_112_graphics import *

def appStarted(app):
    app.score = 0
    app.topMargin = 35
    app.margin = 5
    app.rows = 10
    app.cols = 10

    app.spacing = 2 # spacing for circle

    app.currentRow = 0
    app.currentCol = 0
    app.goingRight = True

    app.paused = False

    app.isExplosion = False
    app.expRadius = 10
    app.expX = 0
    app.expY = 0
    app.color = "blue"

def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - (app.margin + app.topMargin)
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows

    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.topMargin + row * cellHeight
    y1 = app.topMargin + (row+1) * cellHeight
    
    return (x0, y0, x1, y1)

def mousePressed(app, event):
    if not app.isExplosion:
        app.expY = event.y
        app.expX = event.x
        app.isExplosion = True

def keyPressed(app, event):
    if event.key.isdigit():
        N = int(event.key)
        if N < 4:
            app.rows = (N+10)
            app.cols = (N+10)
        else: 
            app.rows = N
            app.cols = N
    if (event.key == 'p'):
        app.paused = not app.paused
    elif (event.key == 's') and app.paused:
        doStep(app)
    elif (event.key == 'r'):
        app.score = 0 
        app.currentCol = 0 
        app.currentRow = 0
        app.goingRight = True
        app.color = "blue"

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**(1/2)

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)
    if d <= r1+r2:
        return True

def explosionIntersectsDot(app):
    if app.isExplosion:
        gridWidth  = app.width - 2*app.margin
        gridHeight = app.height - (app.margin + app.topMargin)
        cellWidth = gridWidth / app.cols
        cellHeight = gridHeight / app.rows
        radius = cellWidth / 2
        x = (app.currentCol) * cellWidth + cellWidth / 2 
        y = (app.currentRow) * cellHeight + cellHeight / 2
        print(app.expX, app.expY, app.expRadius, x, y, radius)
        if circlesIntersect(app.expX, app.expY, app.expRadius, x, y, radius):
            return True

def moveDot(app):
    if app.currentRow > app.rows - 1:
        app.currentRow = 0
    if app.goingRight:
        if app.currentCol > app.cols - 2:
            app.goingRight = False
            app.currentRow += 1
        else:
            app.currentCol += 1
    elif not app.goingRight:
        if app.currentCol < 1:
            app.goingRight = True
            app.currentRow += 1
        else:
            app.currentCol -= 1
    

def growExplosion(app):
    if app.expRadius < 50:
        app.expRadius += 10 
    else:
        app.expRadius = 0
        app.isExplosion = False


def timerFired(app):
    if not app.paused:
        doStep(app)

def doStep(app):
    moveDot(app)
    if app.isExplosion:
        growExplosion(app)
        if explosionIntersectsDot(app):

            app.currentCol = 0
            app.currentRow = 0
            app.goingRight = True
            if app.color == "blue":
                app.score += (app.expRadius)//10
                app.color = "red"               
            else:
                app.score += 10
                app.color = "blue"
            app.expRadius = 0
            app.isExplosion = False
        else: 
            if app.expRadius >= 50:
                if app.score > 0:
                    app.score -= 1

def drawTitleAndScore(app, canvas):
    canvas.create_text(app.width/2, 10, text = "Hw5 Game!")
    canvas.create_text(30, 10, text = f"Score: {app.score}")

def drawGrid(app, canvas):
    xspacing = (app.width - (2 * app.margin))/app.cols
    yspacing = (app.height - (app.topMargin + app.margin))/app.rows
    for line in range(app.rows + 1):
        xcoor = (xspacing * line) + app.margin
        ycoor = app.height - ((yspacing * line) + app.margin)
        canvas.create_line(xcoor, app.topMargin, xcoor, app.height - app.margin)
        canvas.create_line(app.margin, ycoor, app.width - app.margin, ycoor)

def drawDot(app, canvas):
    x0, y0, x1, y1 = getCellBounds(app, app.currentRow, app.currentCol)
    canvas.create_oval(x0 + app.spacing, y0 + app.spacing,
                       x1 - app.spacing, y1 - app.spacing,
                       fill = app.color)

def drawExplosion(app, canvas):
    if app.isExplosion:
        canvas.create_oval(app.expX - app.expRadius, app.expY - app.expRadius, 
                           app.expX + app.expRadius, app.expY + app.expRadius,
                           fill = "orange")

def redrawAll(app, canvas):
    drawTitleAndScore(app, canvas)
    drawGrid(app, canvas)
    drawExplosion(app, canvas)
    drawDot(app, canvas)

def main():
    cs112_n22_week2_linter.lint()
    runApp(width=510, height=540)

if __name__ == '__main__':
    main()