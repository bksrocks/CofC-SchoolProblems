# Name: Barbara Szwabowski
# lab8_szwabowski.py


# 1 - The function format_practice() contains several print statements.
# Fill in the blanks with code that will make statement print the
# expected output.
def format_practice():
    print("This function displays several formatted strings.")

    print("The value of {} is {}.".format('x', 19))
    # Expected: The value of x is 19.

    print("It's raining {1} and {0}".format('dogs', 'cats'))
    # Expected: It's raining cats and dogs

    print("My name is {0}, {1} {0}".format("Bond", "James"))
    # Expected: My name is Bond, James Bond

    print("{0:.2f} {1:.3f}".format(2.3, 0.4567))
    # Expected: 2.30 0.457

    print("Time left:{0:02.0f}:{1:05.2f}".format(3, 7.4589))
    # Expected: Time left: 03:07.46

    print("{0} {1}: {2:.2f}".format("Steph", "Curry", 43.75432))
    # Expected: Steph Curry: 43.75


# 2 - Write a function rename() that asks the user to enter a string in
# lower_snake_case and displays it back in lowerCamelCase
def rename():
    lower_case = input("Enter lower_case string: ")
    to_convert = lower_case.split('_')

    print(to_convert[0], end="")
    for word in to_convert[1:]:
        print(word.capitalize(), end="")


# 3 - (a) Write a function caesar() that asks the user to enter a
# message and an integer key, and then encrypts the message with the key
# by shifting it through the ASCII character set.
def caesar():
    message = input("Enter the message to be encrypted: ")
    key = eval(input("Enter the message's key: "))

    encrypted_message = ''
    for char in message:
        encrypted_message += chr(ord(char) + key)

    print("You've got mail!\n {}".format(encrypted_message))


# (b) The attached file secret.txt contains a ciphertext that has been
# encrypted with a special Caesar cipher where the key is the length of
# the message. Write a function secret() that reads the contents of the
# file, decrypts it, and displays the recovered message.
def secret():
    with open("secret.txt", 'r') as message_f:
        message = message_f.read()
        key = len(message)
        decrypted_message = ''
        for char in message:
            decrypted_message += chr(ord(char) - key)
        print("Recovered message: {}".format(decrypted_message))


# (c) You may have noticed that using a large key produces a ciphertext
# with non-letter characters. A wrapping Caesar cipher is one in which
# characters shifted past Z wrap back around to A. For example, the
# message “XYZ” encrypted with a key of 3 would produce the ciphertext
# “ABC”. Write a function wrapping() that works as in part (a) except
# that it performs a wrapping Caesar cipher. You may assume the message
# contains only uppercase letters.
def wrapping():
    message = input("Enter the message to be encrypted: ")
    key = eval(input("Enter the message's key: "))

    encrypted_message = ''
    for char in message:
        output = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        encrypted_message += output

    print(encrypted_message)


# 4 - (a) You have been tasked with decrypting the following ciphertext,
# which appears to be a binary string partitioned into 6-bit segments:
# 001111 011101 010110 011000 001010 000110 010010 011001
# You have also recovered a Bible with certain words highlighted. When
# compiled together and sorted, the following list was produced:
# ['ANYTHING', 'AS', 'BUT', 'CAN', 'COUNT', 'CREATE', 'DIFFICULTY',
#  'DO', 'DOES', 'END', 'EVERY', 'GO', 'HOW', 'IMAGINE', 'IMPOSSIBLE',
#  'IN', 'IS', 'IT', 'LIES', 'LIFE', 'LONG', 'MATTER', 'MIDDLE', 'NOT',
#  'OF', 'OPPORTUNITY', 'SLOWLY', 'STOP', 'THAT', 'THE', 'THOSE', 'WHO',
#  'YEARS', 'YOU', 'YOUR']
def book_cipher():
    message = "001111 011101 010110 011000 001010 000110 010010 011001"
    book = ['ANYTHING', 'AS', 'BUT', 'CAN', 'COUNT', 'CREATE',
            'DIFFICULTY', 'DO', 'DOES', 'END', 'EVERY', 'GO', 'HOW',
            'IMAGINE', 'IMPOSSIBLE', 'IN', 'IS', 'IT', 'LIES', 'LIFE',
            'LONG', 'MATTER', 'MIDDLE', 'NOT', 'OF', 'OPPORTUNITY',
            'SLOWLY', 'STOP', 'THAT', 'THE', 'THOSE', 'WHO', 'YEARS',
            'YOU', 'YOUR']
    binary = message.split()
    bin_list = binary_list(64)

    decrypted_index = []
    for number in binary:
        decrypted_index.append(bin_list.index(number))

    decrypted_message = ''
    for number in decrypted_index:
        decrypted_message += book[int(number)] + " "

    print(decrypted_message)


def binary_list(n):
    from math import log2
    numbers = []
    for i in range(n):
        # bin() converts a number to binary, but without leading 0's
        # str.zfill() left-pads a string with zeros
        number = bin(i)[2:].zfill(int(log2(n)))
        numbers.append(number)
    return numbers


# (b) You are a military contractor that has been tasked with decrypting
# the following ciphertext, which appears to be a list of integers
# separated by dashes:
# 113100-364637-261587
# You have reason to believe that the codebook is an English dictionary.
# Write a function dict_cipher() that reads the attached dictionary.txt
# into a list, uses it to decrypt the ciphertext, and write the result
# to a new file called message.txt.
def dict_cipher():
    message = "113100-364637-261587".split('-')

    with open("dictionary.txt", 'r') as dictionary_file:
        with open("message.txt", 'w') as output_f:
            dictionary = dictionary_file.read().split("\n")

            for number in message:
                print(dictionary[int(number)], end=" ", file = output_f)


def main():
    # format_practice()
    # rename()
    # caesar()
    # secret()
    # wrapping()
    # book_cipher()
    # binary_list()
    dict_cipher()


main()
