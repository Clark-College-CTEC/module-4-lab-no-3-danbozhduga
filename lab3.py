# Lab No. 3
# CTEC 121
# Daniel Bozhduga

import graphics

def snowman():
    # create the graphics window
    win = graphics.GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    circle1 = graphics.Circle(graphics.Point(300,150), 50)
    circle2 = graphics.Circle(graphics.Point(300,250), 50)
    circle3 = graphics.Circle(graphics.Point(300,350), 50)
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eye1 = graphics.Circle(graphics.Point(285,130), 5)
    eye2 = graphics.Circle(graphics.Point(315,130), 5)
    eye1.setFill('black')
    eye2.setFill('black')
    eye1.draw(win)
    eye2.draw(win)


    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
    nose = graphics.Polygon(graphics.Point(290,150), graphics.Point(310,150), graphics.Point(300,200))
    nose.setFill('orange')
    nose.draw(win)



    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = graphics.Rectangle(graphics.Point(270,100), graphics.Point(330,70))
    hat.setFill('black')
    hat.draw(win)


    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    hatline = graphics.Line(graphics.Point(250,100), graphics.Point(350, 100))
    hatline.setWidth("5")
    hatline.draw(win)



    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()