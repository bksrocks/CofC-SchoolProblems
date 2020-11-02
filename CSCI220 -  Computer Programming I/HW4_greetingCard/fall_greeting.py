# Name: Barbara Szwabowski
# fall_greeting.py

# Purpose: The following program creates a thanksgiving card.
# Certification of Authenticity: I certify that this lab is entirely my
# own work.

# Input: User's name and mouse clicks.

# Output: A window with a card and a message addressed to the user.

from graphics import *
from time import *
from random import *


def main():
    # creates the window
    win = GraphWin("Happy Thanksgiving", 800, 600)

    # sets the window's background
    win.setBackground(color_rgb(57, 83, 4))
    background = Image(Point(400, 300), "background.gif")
    background.draw(win)

    oval1 = Oval(Point(25, 50), Point(775, 550))
    oval1.setFill(color_rgb(72, 44, 21))
    oval1.setOutline(color_rgb(72, 44, 21))
    oval1.draw(win)

    oval2 = Oval(Point(35, 60), Point(765, 540))
    oval2.setFill(color_rgb(194, 40, 35))
    oval2.setOutline(color_rgb(194, 40, 35))
    oval2.draw(win)

    oval3 = Oval(Point(45, 70), Point(755, 530))
    oval3.setFill(color_rgb(174, 70, 56))
    oval3.setOutline(color_rgb(174, 70, 56))
    oval3.draw(win)

    # displays greetings and asks for user's name and click as input
    pumpkin = Image(Point(400, 325), "pumpkin.gif")
    pumpkin.draw(win)
    greetings = Text(Point(400, 270), "Enter your name \nand click for "
                                      "a surprise!")
    greetings.setSize(24)
    greetings.setStyle("bold")
    greetings.setTextColor(color_rgb(194, 40, 35))
    greetings.setFace("arial")
    greetings.draw(win)

    # box for name input
    name_box = Entry(Point(400, 330), 15)
    name_box.setFill(color_rgb(245, 164, 51))
    name_box.setTextColor(color_rgb(194, 40, 35))
    name_box.setFace("arial")
    name_box.setStyle("bold")
    name_box.draw(win)

    # wait for a click to show the surprise message
    win.getMouse()
    user_name = name_box.getText()
    pumpkin.undraw()
    greetings.undraw()
    name_box.undraw()

    # adds the message's image
    peanuts = Image(Point(400, 350), "thanksgiving.gif")
    peanuts.draw(win)

    # creates a message
    message = ['H', 'A', 'P', 'P', 'Y', ' ', 'T', 'H', 'A', 'N', 'K',
               'S', 'G', 'I', 'V', 'I', 'N', 'G', '!']
    y = 220

    for letter in message:
        letter_out = Text(Point(y, 150), letter)
        letter_out.setStyle("bold")
        letter_out.setSize(36)
        letter_out.setFace("arial")
        letter_out.setTextColor(color_rgb(245, 164, 51))
        letter_out.draw(win)
        sleep(0.2)
        y += 21
        letter_out.undraw()

    # prints out a personalized message to the user
    text_output = Text(Point(400, 150), "HAPPY THANKSGIVING,\n" +
                       user_name.upper() + "!")
    text_output.setTextColor(color_rgb(245, 164, 51))
    text_output.setSize(32)
    text_output.setStyle("bold")
    text_output.setFace("arial")
    text_output.draw(win)

    # instructs user on how to stop animation
    button = Rectangle(Point(702, 3), Point(798, 17))
    button.setOutline(color_rgb(245, 164, 51))
    button.setFill(color_rgb(250, 222, 26))
    button.draw(win)
    text_output = Text(Point(750, 10), "Click to stop")
    text_output.setTextColor(color_rgb(194, 40, 35))
    text_output.setSize(10)
    text_output.setStyle("bold")
    text_output.setFace("arial")
    text_output.draw(win)

    # this loop generates random sparkle decorations on the screen and
    # changes the color of the main oval

    # I am not sure if we are allowed to use 'while', I did because it
    # was used in the 'randomCircle.py' file. But if we're not allowed
    # I would replace it with the for loop bellow.

    # for i in range(200):
    while not win.checkMouse():
        # defines the parameters of the 'sparkles'
        x_coord1 = randint(0, 800)
        y_coord1 = randint(0, 600)
        sparkle1 = Text(Point(x_coord1, y_coord1), "*")
        sparkle1.setSize(20)
        sparkle1.setStyle("bold")
        sparkle1.setTextColor(color_rgb(245, 164, 51))

        x_coord2 = randint(0, 800)
        y_coord2 = randint(0, 600)
        sparkle2 = Text(Point(x_coord2, y_coord2), "*")
        sparkle2.setSize(20)
        sparkle2.setStyle("bold")
        sparkle2.setTextColor(color_rgb(245, 164, 51))

        x_coord3 = randint(0, 800)
        y_coord3 = randint(0, 600)
        sparkle3 = Text(Point(x_coord3, y_coord3), "*")
        sparkle3.setSize(20)
        sparkle3.setStyle("bold")
        sparkle3.setTextColor(color_rgb(245, 164, 51))

        x_coord4 = randint(0, 800)
        y_coord4 = randint(0, 600)
        sparkle4 = Text(Point(x_coord4, y_coord4), "*")
        sparkle4.setSize(20)
        sparkle4.setStyle("bold")
        sparkle4.setTextColor(color_rgb(245, 164, 51))

        x_coord5 = randint(0, 800)
        y_coord5 = randint(0, 600)
        sparkle5 = Text(Point(x_coord5, y_coord5), "*")
        sparkle5.setSize(20)
        sparkle5.setStyle("bold")
        sparkle5.setTextColor(color_rgb(245, 164, 51))

        x_coord6 = randint(0, 800)
        y_coord6 = randint(0, 600)
        sparkle6 = Text(Point(x_coord6, y_coord6), "*")
        sparkle6.setSize(20)
        sparkle6.setStyle("bold")
        sparkle6.setTextColor(color_rgb(245, 164, 51))

        # draws the sparkles
        sparkle1.draw(win)
        sparkle2.draw(win)
        sparkle3.draw(win)
        sparkle4.draw(win)
        sparkle5.draw(win)
        sparkle6.draw(win)

        # first round of color changes in the oval
        oval2.setFill(color_rgb(72, 44, 21))
        oval2.setOutline(color_rgb(72, 44, 21))
        oval3.setFill(color_rgb(194, 40, 35))
        oval3.setOutline(color_rgb(194, 40, 35))
        oval1.setFill(color_rgb(174, 70, 56))
        oval1.setOutline(color_rgb(174, 70, 56))

        sleep(0.1)

        # changes the color of the sparkles
        sparkle1.setTextColor(color_rgb(250, 222, 26))
        sparkle2.setTextColor(color_rgb(250, 222, 26))
        sparkle3.setTextColor(color_rgb(250, 222, 26))
        sparkle4.setTextColor(color_rgb(250, 222, 26))
        sparkle5.setTextColor(color_rgb(250, 222, 26))
        sparkle6.setTextColor(color_rgb(250, 222, 26))

        # second round of color changes in the oval
        oval3.setFill(color_rgb(72, 44, 21))
        oval3.setOutline(color_rgb(72, 44, 21))
        oval1.setFill(color_rgb(194, 40, 35))
        oval1.setOutline(color_rgb(194, 40, 35))
        oval2.setFill(color_rgb(174, 70, 56))
        oval2.setOutline(color_rgb(174, 70, 56))

        sleep(0.1)

        # erases the 'sparkles'
        sparkle1.undraw()
        sparkle2.undraw()
        sparkle3.undraw()
        sparkle4.undraw()
        sparkle5.undraw()
        sparkle6.undraw()

        # third round of color changes in the oval - returns to original
        oval1.setFill(color_rgb(72, 44, 21))
        oval1.setOutline(color_rgb(72, 44, 21))
        oval2.setFill(color_rgb(194, 40, 35))
        oval2.setOutline(color_rgb(194, 40, 35))
        oval3.setFill(color_rgb(174, 70, 56))
        oval3.setOutline(color_rgb(174, 70, 56))

        sleep(0.1)

    # instructs user on how to exit the program
    text_output.setText("Click to exit")

    # closes the window when user clicks on the screen
    win.getMouse()
    win.close()


main()
