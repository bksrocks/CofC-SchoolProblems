# Name: Barbara Szwabowski
# lab3_szwabowski.py
# Purpose: Solves problems assigned in Lab 2

def calc_pay():
    print("This function calculates an employee's gross pay.")

    # asks user to enter hours worked and pay rate
    hours_worked = eval(input("Enter the number of hours worked: "))
    pay_rate = eval(input("Enter the pay rate: "))

    # calculates total pay
    total_pay = hours_worked * pay_rate

    # outputs total pay
    print("-------------------------------------")
    print("Total pay: $", round(total_pay, 2), sep="")


def power():
    print("This function calculates the power of some base raised to "
          "some exponent.")

    # asks user for input on base and exponent numbers
    power_base, power_exponent = eval(input("Enter the base and "
                                            "exponent numbers, "
                                            "separated by comma: "))

    # assigns the value for base to a constant
    POWER_BASE = power_base

    # calculates the power based on input
    for i in range(power_exponent-1):
        power_base = power_base * POWER_BASE

    # prints the results
    print(POWER_BASE, "^", power_exponent, "=", power_base)


def approx_sqrt():
    print("This function calculates the approximated square root of a "
          "number with the precision defined by the user")

    # asks user for input on base and refine times
    square_base = eval(input("Enter the number to be square root: "))
    refine_times = eval(input("Inform the number of times to refine "
                              "the guess: "))

    # calculates initial guess
    guess = square_base / 2

    # calculates remaining guesses
    for i in range(refine_times):
        guess = (guess + (square_base / guess)) / 2

    # prints the results
    print("The square root of", square_base, "is approximately",
          round(guess, 2))


def alternate():
    print("This function prints a sequence of 0s and 8s as many times "
          "as defined by the user")

    # asks user how many numbers should be printed
    number_terms = eval(input("Enter the amount of numbers you want "
                              "printed: "))

    # decides if it is an even or odd number
    # normal = int(number_terms / 2)
    # extra = number_terms % 2
    #
    # # prints for even numbers
    # for i in range(normal):
    #     print("0", end=" ")
    #     print("8", end=" ")
    #
    # # prints the remaining odd number
    # for i in range(extra):
    #     print("0", end=" ")
    for i in range(number_terms):
        print((i % 2)*8, end="")
    print()

def flag():
    print("This function prints the USA flag with '*' and '=' "
          "characters.")

    # the first loop goes over the lines with different characters
    for j in range(5):
        # first it prints '*'
        for m in range(6):
            print("*", end=" ")
        # then it prints '='
        for n in range(33):
            print("=", end="")
        print()

    # the second loop prints the lines with the same characters
    for k in range(5):
        for p in range(45):
            print("=", end="")
        print()


def triangle():
    print("This function prints a triangle made of '*' and empty "
          "spaces.")

    # prints 10 rows, in each print the number of empty spaces
    # increase and '*' decrease
    for i in range(10):
        for j in range(0, i):
            print(" ", end=" ")
        for k in range(i, 10):
            print("*", end=" ")
        print()


def receipt():
    print("This function prints a receipt of a purchase made by user.")

    # ======= PART A =======
    # item = input("Enter item purchased: ")
    # price = eval(input("Enter the price of the item: "))
    # quantity = eval(input("Quantity bought: "))
    # total_item = price * quantity
    #
    # print("\n\n")
    # print("RECEIPT")
    # print(quantity, " ", item, " @ $", round(price, 2), " = ",
    #       round(total_item, 2), sep="")
    # print("---------------------------------")
    # print("TOTAL: $", total_item, sep="")

    # ======= PART B =======
    # item1 = input("Enter item purchased: ")
    # price1 = eval(input("Enter the price of the item: "))
    # quantity1 = eval(input("Quantity bought: "))
    # total_item1 = price1 * quantity1
    # item2 = input("Enter item purchased: ")
    # price2 = eval(input("Enter the price of the item: "))
    # quantity2 = eval(input("Quantity bought: "))
    # total_item2 = price2 * quantity2
    #
    # total_items = total_item1 + total_item2
    #
    # print("\n\n")
    # print("RECEIPT")
    # print(quantity1, " x ", item1, " @ $", round(price1, 2), " = ",
    #       round(total_item1, 2), sep="")
    # print(quantity2, " x ", item2, " @ $", round(price2, 2), " = ",
    #       round(total_item2, 2), sep="")
    # print("---------------------------------")
    # print("TOTAL: $", total_items, sep="")

    # ======= PART C =======
    # asks user for number of items purchased
    number_items = eval(input("Enter the number of items purchased: "))
    # creates list that will be used to store groceries information
    groceries = []
    total_purchase = 0

    # asks user for information on items purchased and store them in
    # the list 'groceries
    for i in range(number_items):
        item = input("Enter item purchased: ")
        price = eval(input("Enter the price of the item: "))
        quantity = int(input("Quantity bought: "))
        total_item = price * quantity
        groceries.append(quantity)
        groceries.append(item)
        groceries.append(price)
        groceries.append(total_item)
        total_purchase = total_purchase + total_item

    # prints the receipt
    print("\n")
    print("       ###   RECEIPT   ###       ")
    print("---------------------------------")
    for j in range(0, len(groceries), 4):
        print(groceries[j], " x ", groceries[j+1], " @ $",
              round(float(groceries[j+2]), 2), " = ",
              round(float(groceries[j+3]), 2), sep="")
    print("---------------------------------")
    print("TOTAL: $", round(total_purchase, 2), sep="")


def main():
    # pass
    # calc_pay()
    # power()
    # approx_sqrt()
    alternate()
    # flag()
    # triangle()
    # receipt()


main()
