# Name: Barbara Szwabowski
# lab7_szwabowski.py

from graphics import *


def warmup():
    # Write a function warmup() that begins with the following line:
    values = [5, "hi", 2.5, "there", Point(5, 10), "7.2"]
    # Then, the function should display each of the following using
    # only the above list:

    # (a) The string "hithere"
    print(values[1] + values[3])
    # (b) The string "hihihihihi"
    print(values[1] * values[0])
    # (c) The list [2.5, "there", Point(5, 10)]
    print(values[2:5])
    # (d) The list ["hi", "there", "7.2"]
    new_list =[]
    for i in range(1, len(values), 2):
        new_list.append(values[i])
    print(new_list)
    # (e) The list [2.5, 5, 7.2], where 7.2 is a float rather than a string
    numbers = [values[2], values[0], float(values[-1])]
    print(numbers)
    # (f) The sum of 5, 2.5, and 7.2
    total = 0
    for i in numbers:
        total += i
    print(total)
    # (g) The number of items in the list
    print(len(values))


def address():
    # Write a function address() that asks the user to enter four whole
    # numbers separated by commas, and displays them separated by
    # periods (the format of an IPv4 address). For example, the input
    # 127, 0, 0, 1 should produce the address 127.0.0.1 (note that there
    # is no period at the end).

    ip_num = input("Enter four whole numbers separated by commas: ")
    print('.'.join(ip_num.split(",")))


def search():
    # Write a function search() that that asks the user to enter a
    # sentence and a word in the sentence to search for. The function
    # should then display the position of the start of the word in the
    # sentence. For example, if the user enters the string 'You're a
    # wizard, Harry'. and asks to search for “wizard”, the program
    # should display 10 because “wizard” begins at the 10th character.
    # Remember that Python uses 0-based indexing, so position 0 should
    # be displayed as 1 for the user.

    sentence = input("Enter a sentence: ")
    word = input("Enter the word to be searched: ")
    print(sentence.find(word) + 1)


def emails():
    # Write a function emails() that asks the user how many usernames
    # will be entered. For each username, it should generate the
    # corresponding email by adding “@g.cofc.edu” to the end. After all
    # the usernames have been entered, the function should display the
    # generated emails in a comma-separated list. For example:
    input_names = eval(input("How many usernames will be entered: "))

    list_emails = []
    for i in range(input_names):
        username = input("Enter user name #" + str(i + 1) + ": ")
        email = username + "@g.cofc.edu"
        list_emails.append(email)
    print("Emails: " + ', '.join(list_emails))


def count_words():
    # Write a function count_words() that asks the user how many
    # sentences will be entered. It should then prompt the user to enter
    # each sentence and then display the number of words in it. For
    # example, the sentence The quick brown fox jumps over the lazy dog.
    # has 9 words.

    input_sentences = eval(input("How many sentences will be entered: "))

    for i in range(input_sentences):
        sentence = input("Enter sentence #" + str(i + 1) + ": ")
        # count = len(sentence.split(" "))
        # print(sentence, "has", count, "words.")
        print(sentence, "has", len(sentence.split(" ")), "words.")


def word_average():
    # Write a function word_avg() that asks the user to enter a sentence
    # and then displays the average word length. Round the result to 1
    # digit. For example, the sentence The quick brown fox jumps over the
    # lazy dog. has an average word length of 3.9.

    sentence = input("Enter a sentence: ")
    words = sentence.split(" ")
    # chars = []
    chars = 0
    for word in words:
        # chars.append(len(word))
        chars += len(word)
    # average = chars / len(words)
    # print(round(average))
    print(round(chars/len(words), 1))


def main():
    # warmup()
    # address()
    # search()
    # emails()
    # count_words()
    word_average()


main()
