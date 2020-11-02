# Name: Barbara Szwabowski
# lab10_szwabowski.py


from graphics import *
import math


def fizzbuzz():
    """The function fizzbuzz() prints the numbers from 1 up to a maximum
     entered by the user, but every multiple of 3 is replaced with the
     word “Fizz” and every multiple of 5 is replaced with the word
     “Buzz”. Any number that is a multiple of both 3 and 5 should is
     replaced by “FizzBuzz”."""

    user_range = eval(input("Enter the maximum number: "))
    if user_range < 20:
        print("Too low!")
    elif user_range > 100:
        print("Too high!")
    else:
        for number in range(1, user_range):
            if (number % 3) == 0 and (number % 5) == 0:
                print("FizzBuzz")
            elif (number % 3) == 0 and (number % 5) != 0:
                print("Fizz")
            elif (number % 3) != 0 and (number % 5) == 0:
                print("Buzz")
            else:
                print(number)


def odd(x):
    """This function tests if a number is odd"""

    if x % 2 != 0:
        return True
    else:
        return False


def eligible(weight, wins):
    """This functions judges if a player is eligible to be a starter in
    the wrestling team based on its weight and wins"""

    if wins >= 20 or weight >= 200 or (150 < weight < 160 and wins >= 5):
        return True
    else:
        return False


def letter(score):
    """This functions converts number to letter grades"""

    if score >= 90:
        return "A"
    elif 80 < score < 89:
        return "B"
    elif 70 < score < 79:
        return "C"
    elif 60 < score < 69:
        return "D"
    else:
        return "F"


def digit_pair(x, y, z):
    """This function compares 3 numbers and returns True if any two have
    the same last digit"""

    if (x % 10) == (y % 10) or (x % 10) == (z % 10) or \
            (y % 10) == (z % 10):
        return True
    else:
        return False


def distance(point1, point2):
    """This function calculates the distance between two points"""

    dist = math.sqrt((point2.getX()-point1.getX()) ** 2 +
                     (point2.getY()-point1.getY()) ** 2)
    return dist


def color_circle(dist):
    """This function defines the color of a circle based on its radius"""

    if dist < 30:
        return "red"
    else:
        return "green"


def overlap(list_circles):
    """This function evaluates if circles in a list overlap and returns
    a message if they do"""

    output = []
    for i in range(len(list_circles) - 1):
        circle1 = list_circles[i]
        circle2 = list_circles[i+1]
        rad1 = distance(circle1[0], circle1[1])
        rad2 = distance(circle2[0], circle2[1])
        dist = distance(circle1[0], circle2[0])
        if dist <= (rad1 + rad2):
            message = "Circle " + str(i+1) + " overlaps with circle " + \
                      str(i+2)
            output.append(message)
    return output


def circles():

    # Creates window
    width = 800
    height = 800
    win = GraphWin("Circles", width, height)

    # Provides instruction
    instruction = Text(Point(400, 25), "To draw a circle click once "
                                       "for its center and again for "
                                       "its radius.")
    instruction.setSize(15)
    instruction.draw(win)

    circles_list = []

    # Draws the circles
    for i in range(5):
        center = win.getMouse()
        outline = win.getMouse()
        radius = distance(center, outline)

        # Adds circle information to list for overlap comparison
        circle = [center, outline]
        circles_list.append(circle)

        circle = Circle(center, radius)
        circle.setFill(color_circle(radius))
        circle.draw(win)

    # Provides instruction on how to exit
    instruction.setText("Click to exit")

    # Prints information on overlaps
    try:
        overlaps = overlap(circles_list)
        bottom = 725

        for item in overlaps:
            overlap_out = Text(Point(400, bottom), item)
            overlap_out.setSize(15)
            overlap_out.draw(win)
            bottom += 15
    except:
        overlap_out = Text(Point(400, 725), "No overlaps")
        overlap_out.setSize(15)
        overlap_out.draw(win)

    # Waits for user's action
    win.getMouse()
    win.close()


def test(name, result, expected):
    """This function evaluates a function test and prints errors if any"""

    if result == expected:
        pass
    else:
        print("Failed: {} (expected {}, got {})".format(name, expected,
                                                        result))


def run_tests():
    """Runs the tests for Lab 10"""

    print("Beginning tests...")

    # fizzbuzz()

    test("Function odd", odd(2), False)
    test("Function odd", odd(3), True)

    test("Function eligible", eligible(210, 0), True)
    test("Function eligible", eligible(100, 22), True)
    test("Function eligible", eligible(155, 5), True)
    test("Function eligible", eligible(150, 0), False)

    test("Function letter", letter(95), "A")
    test("Function letter", letter(85), "B")
    test("Function letter", letter(75), "C")
    test("Function letter", letter(65), "D")
    test("Function letter", letter(55), "F")
    test("Function letter", letter(45), "F")

    test("Function digit_pair", digit_pair(22, 33, 44), False)
    test("Function digit_pair", digit_pair(22, 12, 44), True)
    test("Function digit_pair", digit_pair(22, 14, 44), True)
    test("Function digit_pair", digit_pair(33, 11, 33), True)

    circles()

    print("Testing complete!")


run_tests()
