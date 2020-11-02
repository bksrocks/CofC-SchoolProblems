# Name: Barbara Szwabowski
# lab5.py

from graphics import *
from math import *


def converter():
    # Authors: RoxAnn H. Stalvey, Walter Pharr, Anthony Morrell
    # Illustrates getting numeric input through graphics window

    width = 300
    height = 200
    win = GraphWin("Unit Conversion", width, height)

    # Describes the program
    program_descrip = Text(Point(150, 25), "This program converts "
                                           "values from millimeters to "
                                           "inches ")
    program_descrip.draw(win)

    # Specify the message for the input box
    box_desc = Text(Point(125, 50), "Number (millimeters) to be "
                                    "converted: ")
    box_desc.draw(win)

    # Create the Entry object and set its default text to a number
    #   allowing the user to see what type of value is expected
    input_box = Entry(Point(250, 50), 5)
    input_box.setText("0")
    input_box.draw(win)

    # Create a Text object for outputting the result
    output = Text(Point(150, 150), "")
    output.draw(win)

    # This button isn't necessary, but it makes a nice point for the user
    #   to click. If you click anywhere in the window, the code reacts
    #   the same way.
    btn_x = width / 2
    btn_y = height / 2
    button = Text(Point(btn_x, btn_y), "Convert")
    button.draw(win)
    border = Rectangle(Point(btn_x - 35, btn_y - 20), Point(btn_x + 35,
                                                            btn_y + 20))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover input and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    millimeters = eval(input_box.getText())
    inches = millimeters / 25.4

    # Display output and change button
    output.setText(str(millimeters) + " millimeters equals to " +
                   str(round(inches, 2)) + " inches")
    button.setText("Quit")

    # Wait for another click to exit
    win.getMouse()
    win.close()


def target():
    width = 500
    height = 500
    win = GraphWin("Target", width, height)
    win.setBackground("gray")
    center = Point(250, 250)

    white_circle = Circle(center, 250)
    white_circle.setFill("white")
    white_circle.setOutline("white")
    white_circle.draw(win)
    black_circle = Circle(center, 200)
    black_circle.setFill("black")
    black_circle.draw(win)
    blue_circle = Circle(center, 150)
    blue_circle.setFill("blue")
    blue_circle.setOutline("blue")
    blue_circle.draw(win)
    red_circle = Circle(center, 100)
    red_circle.setFill("red")
    red_circle.setOutline("red")
    red_circle.draw(win)
    yellow_circle = Circle(center, 50)
    yellow_circle.setFill("yellow")
    yellow_circle.setOutline("yellow")
    yellow_circle.draw(win)

    win.getMouse()
    win.close()


def map_plan():
    width = 800
    height = 600
    win = GraphWin("Complex Location Planner", width, height)

    # Draw the background map
    # Make sure that north-charleston.gif is in the same folder as
    #   this Python file
    background = Image(Point(width/2, height/2), "north-charleston.gif")
    background.draw(win)

    # Add your code here:

    # Step 1 - draw complex #1
    instruction = Text(Point(400, 25), "To draw the first complex, "
                                       "click on the corners of the "
                                       "rectangle to be draw")
    instruction.setFace("helvetica")
    instruction.setStyle("bold")
    instruction.setSize(20)
    instruction.draw(win)

    complex_1_p1 = win.getMouse()
    complex_1_p2 = win.getMouse()
    complex_1 = Rectangle(complex_1_p1, complex_1_p2)
    complex_1.setOutline("red")
    complex_1.setFill("red")
    complex_1.draw(win)

    # Step 2 - draw complex #2
    instruction.setText("To draw the second complex, click on the "
                        "corners of the rectangle to be draw")

    complex_2_p1 = win.getMouse()
    complex_2_p2 = win.getMouse()
    complex_2 = Rectangle(complex_2_p1, complex_2_p2)
    complex_2.setOutline("blue")
    complex_2.setFill("blue")
    complex_2.draw(win)

    # Step 3 - Distance between center points
    center_c1 = complex_1.getCenter()
    center_c2 = complex_2.getCenter()

    connecting_line = Line(center_c1, center_c2)
    connecting_line.draw(win)

    distance_px = sqrt(((center_c1.getX() - center_c2.getX()) ** 2) +
                       ((center_c1.getY() - center_c2.getY()) ** 2))
    distance_miles = distance_px / 50
    distance = Text(connecting_line.getCenter(), "distance: " +
                  str(round(distance_miles)) + "miles")
    distance.draw(win)

    # Step 4 - Exit instructions
    instruction.setText("Click to exit.")

    # Wait for click to close the window
    win.getMouse()
    win.close()


def main():
    converter()
    target()
    map_plan()

main()
