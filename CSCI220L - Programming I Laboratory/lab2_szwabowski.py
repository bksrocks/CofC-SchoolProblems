# Name: Barbara Szwabowski
# lab2.py
# Purpose: Solves problems assigned in Lab 2

# module imports
import math

# Sample function to show how to "comment out" function
# calls in main()


def greet():
    print("Hello, world!")


def get_shooting_percent():
    print("This function calculates a shooting percentage in basketball.")

    # ask user for input on how many shots were attempted
    attempted = eval(input("How many shots were attempted? "))
    # ask user for input on how many shots were successful
    successful = eval(input("How many shots were successful? "))

    # calculates the percentage of successful shots
    success_percentage = (successful/attempted) * 100

    # prints the success percentage
    print("The shooting percentage is: ", round(success_percentage, 2), "%.", sep="")


def calc_volume():
    print("This function calculates the volume of a rectangular solid.")

    # # ask user for input on solid's length
    # length = eval(input("Inform the solid's length: "))
    # # ask user for input on solid's width
    # width = eval(input("Inform the solid's width: "))
    # # ask user for input on solid's height
    # height = eval(input("Inform the solid's height: "))

    # ask user for input on solid's length, width and height
    length, width, height = eval(input("Enter the solid's length, width and height separated by commas: "))

    # calculates the volume of the solid
    volume = length * width * height

    # prints the volume of the solid
    print("The volume of the solid is ", round(volume), ".", sep="")


def greet_better():
    print("This function greets the user and shows their age in five years.")

    # ask user for their name
    name = input("What is your name? ")
    # ask user for his age
    age = eval(input("How old are you? "))

    # calculate user's age in 5 years
    five_years = age + 5

    # greet user and shows age in 5 years
    print("Hello " + name + "! In five years, you will be", five_years, "years old.")


def compute_coffee_shop():
    print("This function calculates the price of shipping for coffee orders.")

    # ask user for the amount of coffee purchased
    order = eval(input("How many pounds of coffee are you buying? "))

    # shipping fixed variables
    COFFEE_PRICE_POUND = 7.5
    SHIPPING_PRICE_POUND = 0.44
    FIXED_COST = 3.0

    # calculates total cost
    total_cost = FIXED_COST + (order * (COFFEE_PRICE_POUND + SHIPPING_PRICE_POUND))

    # prints the total cost
    print("The total price of you order is US$", round(total_cost, 2), ".", sep="")


def measure_triangle_area():
    print("This function calculates the area of a triangle.")

    # ask user for the length of the sides of the triangle
    side1, side2, side3 = eval(input("Enter the length of the three sides of the triangle, separated by commas: "))

    # calculates the area of the triangle
    p = (side1 + side2 + side3)/2
    area = math.sqrt(p*(p-side1)*(p-side2)*(p-side3))

    # prints the area of the triangle
    print("The area of the triangle is: ", round(area), ".", sep="")


def sum_squares():
    print("This function calculates the sum of the squares of integers in range defined by user.")

    # ask user for range
    start, end = eval(input("Enter the start and end numbers of your range, separated by commas: "))

    # calculates the sum of squares of integers in the range defined by the user
    squares_sum = 0
    for number in range(start, end+1):
        square = math.pow(number, 2)
        squares_sum = squares_sum + square

    # prints the sum of squares of integers in the range defined by the user
    print("The sum of the square of the integers in this particular range is ", int(squares_sum), ".", sep="")


def main():
    # greet()
    # get_shooting_percent()
    # calc_volume()
    # greet_better()
    # compute_coffee_shop()
    # measure_triangle_area()
    sum_squares()


main()










