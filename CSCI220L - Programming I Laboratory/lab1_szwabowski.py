# CSCI220L - Lab 1 - Sep/02
# Step 6 - a. Write a function, display_sequence(), that displays the numbers 15 through 25.
# b. Write a function, greet(name) , that accepts 1 parameter name and displays “Hello, <name>”.
# For example, calling greet('Momo') should display “Hello, Momo”.

# Author: Barbara Szwabowski

def display_sequence():
    for i in range(15, 26):
        print(i)


def greet(name):
    print("Hello", name)

display_sequence()
print()
greet("Momo")

