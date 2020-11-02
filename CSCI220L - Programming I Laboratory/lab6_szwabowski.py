# Name: Barbara Szwabowski
# lab6_szwabowski.py

def warmup():
    # This function plays with words / characters in a sentence
    string = input("Enter your favorite quote: ")
    length_string = len(string)

# (a) The first and last characters of the string
    print("The first character of your quote is:", string[0],
          "and the last character of your quote is:",
          string[-1])
# (b) The characters in positions 3–6 of the string (inclusive)
    print("The character on position 3 is:", string[2],
          "and the character on position 6 is", string[5])
# (c) The number of characters in the string
    print("The string has", length_string, "characters.")
# (d) The first three characters repeated 10 times
    for i in range(10):
        print(string[:3], end=" ")
    print()
# (e) The string with a comma between each character (Hint: use a loop)
    for letter in string:
        print(letter, end=",")
    print()


def my_len():
    # This function returns the length of a string without using the
    # function len()
    string = input("Enter your favorite quote: ")
    length = 0
    for letter in string:
        length += 1
    print("The string's length is:", length)


def remove():
    # This function removes a character from a sentence according to
    # the index defined by the user
    string = input("Enter your favorite quote: ")
    index = eval(input("Enter an index number: "))
    # string_to_list = []

    # for letter in string:
    #     string_to_list.append(letter)
    string_to_list = list(string)

    for letter in string_to_list[0:index]:
        print(letter, end="")
    for letter in string_to_list[index + 1:]:
        print(letter, end="")
    print()


def add():
    # This function returns the sum of the digits in a number entered
    # by the user
    numbers = input("Enter the number to be added: ")
    sum_numbers = 0

    for number in numbers:
        sum_numbers += int(number)

    print("The sum of the digits of your number is:", sum_numbers)


def reverse():
    # This function returns the user's firs and last name in reverse order
    full_name = input("Enter your first and last name: ")
    full_name_list = full_name.split()

    print(full_name_list[1] + ", " + full_name_list[0])


def caps():
    # This function returns a string in all uppercase
    string = input("Enter your favorite quote: ")
    # string_caps = string.upper()
    # print(string_caps)
    print(string.upper())


def evens():
    # This function returns only the letters with even indexes of a word
    # entered by the user
    word = input("Enter a word: ")

    for letter in range(0, len(word), 2):
        print(word[letter], end="")

    print()


def main():
    # warmup()
    # my_len()
    # remove()
    # add()
    # reverse()
    # caps()
    evens()


main()
