#################################################
# hw4.py
# name: David Chung
# andrew id: dichung
# section: A
#################################################

import cs112_n22_week2_linter
import math, string

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

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

# draw eyes for robot
def drawEyes(x1, y1, radius, canvas):

    # outer eye
    dia = 2 * radius
    canvas.create_oval(x1, y1, x1 + dia, y1 + dia, fill = "#ebe354")
    
    # inner eye
    x1 = x1 + (radius * 0.25) # offset x1 and y1 
                              #so that you can make smaller circle
    y1 = y1 + (radius * 0.25)
    radius *= 0.75
    dia = 2 * radius
    canvas.create_oval(x1, y1, x1 + dia, y1 + dia, fill = "yellow")

    # draw reflection in eye
    x1 += radius / 2
    y1 += radius / 2
    radius *= 0.2
    dia = 2 * radius
    canvas.create_oval(x1, y1, x1 + dia, y1 + dia, fill = "white")

# draws triangle for qatar flag
def drawTriangle(x, y, size, canvas):
    y2 = y + size
    x3 = x + size
    y3 = y + (size/2)
    canvas.create_polygon(x, y, x, y2, x3, y3, fill = "white")




#################################################
# hw4-standard-functions
#################################################

def drawPattern1(canvas, width, height, points):
    xinc = width/points
    yinc = height/points
    for increment in range(0, points + 1):
        x1 = xinc * increment
        y1 = 0
        x2 = width
        y2 = height - (yinc * increment)
        canvas.create_line(x1, y1, x2, y2)
        #same thing but just flip horizontally
        x2 = 0
        y2 = yinc * increment
        canvas.create_line(x1, y1, x2, y2)
        # flip everything we drew vertically
        x1 = width - (xinc * increment)
        y1 = height
        canvas.create_line(x1, y1, x2, y2)
        # flip horizontally
        x2 = width
        y2 = height - (yinc * increment)
        canvas.create_line(x1, y1, x2, y2)
    return 42

def drawNiceRobot(canvas, width, height):
    margin = min(width, height)/10
    topMargin = margin*5 # creates more space at the top

    # draw face background
    canvas.create_rectangle(margin, topMargin, width - margin, 
                            height - margin, fill = "#b6b6b8")

    # draw mouth background 
    # mouth will be drawn a third from the bottom
    yOffset = height * (0.75)
    margin = margin/2
    canvas.create_rectangle(margin, yOffset, width - margin, 
                            height - margin, fill = "#5e5e5e")

    #draw mustache
    mustx1 = margin
    musty1 = yOffset
    mustx2 = margin/2
    musty2 = yOffset * (1.15)
    canvas.create_polygon(# mustache goes above mouth
                          mustx1, musty1,
                          width - mustx1, musty1,
                          width - mustx2, musty2,
                          mustx2, musty2, # make bottom wider
                          fill = "black")


    # draw mouth
    mouthx1 = mustx1 * 2
    mouthy1 = (musty1 * 1.15) + 5 # below mustache
    mouthx2 = width - (margin * 2)
    mouthy2 = height - (margin * 2)

    canvas.create_oval(
                          mouthx1, mouthy1,
                          mouthx2, mouthy2,
                          fill = "white"
    )

    # draw teeth line on mouth
    teethx1 = mouthx1
    teethy = mouthy1 + (mouthy2 - mouthy1)/2 #mouth halfway point
    teethx2 = width - mouthx1
    canvas.create_line(teethx1, teethy, teethx2, teethy)
    
    #draw eyes
    size = margin # set size of eyes to margin length
    drawEyes(margin * 4, yOffset - (margin * 4), size* 2, canvas)
    drawEyes(width - 2 * (margin * 4), yOffset - (margin * 4), size* 2, canvas)
    # width - 2 * margin * 4 because x1,y1 of draw 
    # eyes specifies upper left corner of eyes
    return 42

def drawFlagOfQatar(canvas, x0, y0, x1, y1):
    # Replace all of this with your drawing of the flag of Qatar
    # Also: remember to add the title "Qatar" centered above the flag!

    # find width and height of flag

    width = x1 - x0
    height = y1 - y0

    # create flag background
    canvas.create_rectangle(x0, y0, x1, y1, fill='red', outline = "red")
    font = 'Arial 20 bold' if (x1 - x0 > 150) else 'Arial 12 bold'

    # write qatar
    canvas.create_text((x0+x1)/2, y0 - 20,
                       text='Qatar',
                       font=font)

    # create white triangles

    for triangle in range(9):
        size = height / 9 
        x = x0 + (width / 3)
        y = y0 + (size * triangle)
        drawTriangle(x, y, size, canvas)

    # color remainder of flag white
    canvas.create_rectangle(x0, y0, x0 + (width/3), y1, fill = "white", 
                            outline = "white")

#################################################
# hw4-bonus-functions
# these are optional
#################################################


def drawPattern2(canvas, width, height, points):
    return 42

def drawFancyWheels(canvas, width, height, rows, cols):
    return 42


#################################################
# Test Functions
#################################################

def testDrawPattern1(app, canvas):
    drawPattern1(canvas, app.width, app.height, app.points)
    canvas.create_text(app.width/2, app.height-10, 
          text=('testing drawPattern1' + 
            f'(canvas, {app.width}, {app.height}, {app.points})'))

def testDrawPattern2(app, canvas):
    drawPattern2(canvas, app.width, app.height, app.points)
    canvas.create_text(app.width/2, app.height-10, 
          text=('testing drawPattern2' + 
            f'(canvas, {app.width}, {app.height}, {app.points})'))

def testDrawFlagOfQatar(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='lightYellow')
    drawFlagOfQatar(canvas, 50, 125, 350, 275)
    drawFlagOfQatar(canvas, 425, 100, 575, 200)
    drawFlagOfQatar(canvas, 450, 275, 550, 325)
    canvas.create_text(app.width/2, app.height-20, 
          text="Testing drawFlagOfQatar")
    canvas.create_text(app.width/2, app.height-10, 
          text="This does not need to resize properly!")


def testDrawNiceRobot(app, canvas):
    drawNiceRobot(canvas, app.width, app.height)
    canvas.create_text(app.width/2, app.height-20, 
          text=('Testing drawNiceRobot' +
            f'(canvas, {app.width}, {app.height})'))
    canvas.create_text(app.width/2, app.height-10, 
          text=f'''Comment out these print lines if they mess up your art!''')

def testDrawFancyWheels(app, canvas, rows, cols):
    drawFancyWheels(canvas, app.width, app.height, rows, cols)
    canvas.create_text(app.width/2, app.height-10, 
          text=('testing drawFancyWheels' + 
            f'(canvas, {app.width}, {app.height}, {rows}, {cols})'))


def drawSplashScreen(app, canvas):
    text = f"""
Press the number key for the 
exercise you would like to test!

1. drawPattern1 ({app.points} points)
2. drawNiceRobot
3. drawFlagOfQatar

4. Bonus drawPattern2 ({app.points} points)
5. Bonus drawFancyWheels (1x1)
6. Bonus drawFancyWheels (4x6)


You can press the up or down arrows to change
the number of points for drawPattern1
and drawPattern2 between 3 and 20
"""

    textSize = min(app.width,app.height) // 40
    canvas.create_text(app.width/2, app.height/2, text=text,
                        font=f'Arial {textSize} bold')


def appStarted(app):
    app.lastKeyPressed = None
    app.points = 5
    app.timerDelay = 10**10

def keyPressed(app, event):
    if event.key == "Up":
      app.points = min(20, app.points+1)
      print(f"Increasing points to {app.points}")
      if app.points >= 20: print("Maximum allowed points!")
    elif event.key == "Down":
      app.points = max(3, app.points-1)
      print(f"Decreasing points to {app.points}")
      if app.points <= 3: print("Minimum allowed points!")
    else:
      app.lastKeyPressed = event.key





def redrawAll(app, canvas):
    if app.lastKeyPressed == "1":
      testDrawPattern1(app, canvas)
    elif app.lastKeyPressed == "2":
      testDrawNiceRobot(app, canvas)
    elif app.lastKeyPressed == "3":
      testDrawFlagOfQatar(app, canvas)
    elif app.lastKeyPressed == "4":
      testDrawPattern2(app, canvas)
    elif app.lastKeyPressed == "5":
      testDrawFancyWheels(app, canvas, 1, 1)
    elif app.lastKeyPressed == "6":
      testDrawFancyWheels(app, canvas, 4, 6)
    else:
      drawSplashScreen(app, canvas)

#################################################
# main
#################################################

def main():
    cs112_n22_week2_linter.lint()
    runApp(width=600, height=600)

if __name__ == '__main__':
    main()
