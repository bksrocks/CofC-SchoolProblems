# Name: Barbara Szwabowski
# bmi.py

# Purpose: compute and print a user’s Body Mass Index (BMI), Ideal Body
# Weight (for male), Lean Body Weight (for female) and Body Surface Area
# (BSA). Computes BSA using three different formulas: Mosteller, DuBois
# & DuBois, and Boyd.

# Certification of Authenticity: I certify that this lab is entirely my
# own work.

# Input: User's weight(in kg) and height(in cm).

# Output: Values for user's computed Body Mass Index (BMI), Ideal Body
# Weight (for male), Lean Body Weight (for female),
# and Body Surface Area (BSA) - in Mosteller, DuBois & DuBois, and Boyd.


# makes math library available to use
import math


# function that calculates user's BMI (body mass index)
def func_body_mass_index(height, weight):
    # calculates the body mass index
    body_mass_index = 10000 * (weight / pow(height, 2))
    # prints the calculated body mass index
    print("The user's Body Mass Index is ", round(body_mass_index, 1),
          "kg/m\u00B2.", sep="")


# function that calculates user's ideal body weight
def func_ideal_body_weight(height, weight):
    # calculates the ideal body weight with parameters for males
    ideal_body_weight = 50 + 2.3 * ((height/2.54) - 60)
    # prints the calculated ideal body weight
    print("The user's Ideal Body Weight (men) is ",
          round(ideal_body_weight), "kg.", sep="")


# function that calculates user's lean body weight
def func_lean_body_weight(height, weight):
    # calculates the lean body weight with parameters for females
    lean_body_weight = (1.07 * weight) - 148 * (pow(weight, 2) /
                                                pow(height, 2))
    # prints the calculated lean body weight
    print("The user's Lean Body Weight (women) is ",
          round(lean_body_weight), "kg.", sep="")


# function that calculates user's bsa using Mosteller's formula
def func_bsa_mosteller(height, weight):
    # calculates the body surface area
    bsa_mosteller = math.sqrt((height * weight)/3600)
    # prints the calculated body surface area
    print("The user's Body Surface Area calculated by Mosteller's "
          "formula is ", round(bsa_mosteller, 3), "m\u00B2.", sep="")


# function that calculates user's bsa using DuBois&Dubois' formula
def func_bsa_dubois(height, weight):
    # calculates the body surface area
    bsa_dubois = 0.20247 * pow((height/100), 0.725) * pow(weight, 0.425)
    # prints the calculated body surface area
    print("The user's Body Surface Area calculated by DuBois & DuBois "
          "formula is ", round(bsa_dubois, 3), "m\u00B2.", sep="")


# func_function that calculates user's bsa using Boyd's formula
def func_bsa_boyd(height, weight):
    # calculates the body surface area
    bsa_boyd = 0.0003207 * pow(height, 0.3) * \
               pow(1000 * weight, 0.6721 - 0.0188 * math.log10(weight))
    # prints the calculated body surface area
    print("The user's Body Surface Area calculated by Boyd's formula "
          "is ",  round(bsa_boyd, 3), "m\u00B2.", sep="")


def main():
    # tells user the purpose of the program
    print("This program calculates calculates body surface area and "
          "body mass index based on user's input.")

    # asks user to input height and weight and store in assigned
    # variables
    user_height, user_weight = eval(input("Enter height(cm) and "
                                          "weight(kg) information "
                                          "(separated by comma): "))
    # I am not sure what is the best practice in the case above.
    # Do I just reduce the indentation on the second line or do I leave
    # it like it is?

    # calls function func_body_mass_index and calculates it with values
    # entered by user
    func_body_mass_index(user_height, user_weight)

    # calls function func_ideal_body_weight and calculates it with
    # values entered by user
    func_ideal_body_weight(user_height, user_weight)

    # calls function func_lean_body_weight and calculates it with values
    # entered by user
    func_lean_body_weight(user_height, user_weight)

    # calls function func_bsa_mosteller and calculates it with values
    # entered by user
    func_bsa_mosteller(user_height, user_weight)

    # calls function func_bsa_dubois and calculates it with values
    # entered by user
    func_bsa_dubois(user_height, user_weight)

    # calls function func_bsa_boyd and calculates it with values
    # entered by user
    func_bsa_boyd(user_height, user_weight)


main()
