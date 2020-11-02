# Name: Barbara Szwabowski
# morse_code.py

# Purpose: Creates a program that 'translates' a message to morse code.
# Certification of Authenticity: I certify that this lab is entirely my
# own work.

# Input: User's message.

# Output: User's message in morse code.

from graphics import *


def morse_code(message):
    input_message = message.upper()
    input_message = input_message.split()

    code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
            '..', '.---', '-.-','.-..', '--', '-.','---', '.--.',
            '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
            '-.--', '--..']
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    morse_message = ""

    for word in input_message:
        for letter in word:
            index_letter = alphabet.index(letter)
            morse_message = morse_message + code[index_letter] + " "
        morse_message = morse_message + "   "

    return morse_message


def main():
    # creates the window
    win = GraphWin("Morse Code", 500, 500)

    # sets the window's background
    win.setBackground(color_rgb(136, 171, 179))

    # displays instructions and asks user for input
    instructions = Text(Point(250, 100), "Enter the message to be \n"
                                         "encoded in the box bellow.")
    instructions.setSize(20)
    instructions.setStyle("bold")
    instructions.setTextColor(color_rgb(35, 69, 77))
    instructions.setFace("arial")
    instructions.draw(win)

    # box for message input
    message_box = Entry(Point(250, 200), 50)
    message_box.setFill(color_rgb(2, 169, 207))
    message_box.setTextColor(color_rgb(35, 69, 77))
    message_box.setFace("arial")
    message_box.draw(win)

    # draws encode button
    encode_box = Rectangle(Point(220, 230), Point(280, 260))
    encode_box.setOutline(color_rgb(2, 169, 207))
    encode_box.setFill(color_rgb(35, 69, 77))
    encode_text = Text(encode_box.getCenter(), "ENCODE")
    encode_text.setStyle("bold")
    encode_text.setTextColor(color_rgb(2, 169, 207))
    encode_box.draw(win)
    encode_text.draw(win)

    # wait for a click to encode message
    win.getMouse()
    input_message = message_box.getText()

    # calls function morse_code that will encode the message
    output = morse_code(input_message)

    # outputs the morse code message on user's screen
    message_output = Text(Point(250, 350), output)
    message_output.setTextColor(color_rgb(35, 69, 77))
    message_output.setSize(16)
    message_output.setStyle("bold")
    message_output.setFace("arial")
    message_output.draw(win)

    # instructs user on how to exit the program
    message_output = Text(Point(250, 490), "Click to exit")
    message_output.setTextColor(color_rgb(194, 40, 35))
    message_output.setSize(10)
    message_output.setStyle("bold")
    message_output.setFace("arial")
    message_output.draw(win)

    # closes the window when user clicks on the screen
    win.getMouse()
    win.close()


main()
