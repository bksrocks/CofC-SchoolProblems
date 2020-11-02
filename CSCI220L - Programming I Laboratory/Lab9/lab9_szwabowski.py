# Name: Barbara Szwabowski
# lab9_szwabowski.py

import random
import math


# 1 - (a) Python has a built-in function sum(nums) that returns the sum
# of a list of numbers. Write your own function mean(nums) that accepts
# a list of numbers and returns their mean. You may assume the mean of
# an empty list is zero. Include at least two test cases for mean().
def mean(nums):
    """"Function mean(nums) calculates the mean from a list of numbers

    input: list of numbers

    output: mean of numbers in list"""
    sum_nums = 0
    for number in nums:
        sum_nums += number
    mean_nums = sum_nums / len(nums)

    return mean_nums


# 1 - (b) Write a function mean_str(nums) that accepts a list of strings
# representing numbers and returns their mean rounded to two digits. An
# example input might look like ["10", "15.5"]. Include at least two
# test cases for mean_str().
def mean_str(nums):
    """"Function mean_str(nums) calculates the mean from a list of
    numbers with type str

    input: list of type str numbers

    output: mean of numbers in list"""
    sum_nums = 0
    for number in nums:
        sum_nums += float(number)
    mean_str_nums = round(sum_nums / len(nums), 2)

    return mean_str_nums


# 2 - (a) Write a function get_username(name) that accepts a full name
# as a string and returns the corresponding username in this format:
# last name + first initial + middle initial. The username should be
# all lowercase. For example, “Homer Jay Simpson” should produce
# “simpsonhj”.
def get_username(name):
    """Function get_username(name) converts names in to usernames

    input: full name

    output: username composed of last name + first name initial +
    middle name initial"""
    name_list = name.lower().split()
    username = name_list[-1] + name_list[0][0] + name_list[1][0]

    return username


# 2 - (b) Write a void function usernames(names) that accepts a list of
# full names and converts each name to its corresponding username. The
# function should modify the input list, not return a new one. Include
# at least two test cases for usernames().
def usernames(names):
    """Function usernames(names) generates usernames from a list of
    names

    input: list of full names

    output: list of usernames"""
    for i in range(len(names)):
        username = get_username(names[i])
        names[i] = username

    # return names


# 3 - Write a void function number_lines(file) that accepts a filename,
# reads through the file, and prints each line with its line number in
# front of it. For example:
# 1. To be, or not to be, that is the question:
# 2. Whether 'tis nobler in the mind to suffer
# 3. The slings and arrows of outrageous fortune,
# ...
# Include at least one test case for number_lines() and a corresponding
# .txt file to open. You may use any (short) .txt file as your test file.
def number_lines(file):
    """Function number_lines(fine) prints the lines of a file with its
    index number in front of it

    input: text file

    output: file lines with index number"""
    with open(file, 'r') as text_file:
        index = 1
        for line in text_file.readlines():
            print("{} - {}".format(index, line), end="")
            index += 1
        print()


# 3 - Write a function models(infile, outfile) that reads the infile
# (which is in the above format), calculates the surface area of each
# sphere, writes the surface areas to the outfile, and returns the
# average surface area. The specific format of the outfile is up to you.
# You may wish to write one or more helper functions to keep your
# solution organized and elegant. Finally, include a test case for
# models(). To verify that it works, your code should both display the
# return value and open the outfile to display its contents (you may
# choose to display only the first few lines to keep your test output
# readable).

def surface_area(radius):
    """Function surface_rea(radius) calculates the surface area of
    a sphere.

    input: sphere's radius

    output: sphere's surface area"""
    area = 4 * math.pi * radius ** 2
    return area


def get_rad(line):
    """"Function that gets the sphere's radius from the input file

    input: line of sphere information in the following format:
        Sphere (x=___, y=___, z=___, radius=___, texture=___)

    output: the sphere's radius as a float"""
    measures = line.split(',')
    rad = float(measures[3][8:])
    return rad


def models(infile, outfile):
    """Function models(infile, outfile) takes information from a file,
    uses it to calculate the spheres individual surface area saves it in
    a file; and returns the average surface area of the set of spheres

    input: file with information on a set of spheres in the following
    format: Sphere (x=___, y=___, z=___, radius=___, texture=___)

    output: file with the individual sphere surface area and returns
    the average surface area of the spheres"""
    with open(infile, 'r') as i_file, open(outfile, 'w') as o_file:
        total_surface = 0
        index = 1
        for line in i_file.readlines():
            surface = surface_area(get_rad(line))
            o_file.write("Sphere {} surface area: {:.2f} \n"
                         .format(index, surface))
            total_surface += surface
            index += 1

        surface_average = total_surface / index
        return surface_average


# Function that will hold all required testcases
def test():
    print("Testing mean()")
    mean_test1 = random_numbers(8)  # generates a list of 8 random numbers
    # print(mean_test1)
    print("Eight numbers: {}".format(mean(mean_test1)))
    mean_test2 = random_numbers(10)  # generates a list of 10 random numbers
    # print(mean_test2)
    print("Ten numbers: {}".format(mean(mean_test2)))
    print()

    print("Testing mean_str()")
    mean_str_test1 = random_numbers_str(6)  # generates a list of 6 random numbers with type str
    # print(mean_str_test1)
    print("Six numbers: {}".format(mean_str(mean_str_test1)))
    mean_str_test2 = random_numbers_str(10) # generates a list of 10 random numbers with type str
    # print(mean_str_test2)
    print("Ten numbers: {}".format(mean_str(mean_str_test2)))
    print()

    print("Testing get_username()")
    username_test1 = random_name()  # generates a random name
    print("{} username's is: {}".format(username_test1,
                                        get_username(username_test1)))
    username_test2 = random_name()  # generates a random name
    print("{} username's is: {}".format(username_test2,
                                        get_username(username_test2)))
    print()

    print("Testing usernames()")
    usernames_test1 = random_name_list(7)  # generates a list with 7 random names
    print(usernames_test1)
    usernames(usernames_test1)
    print("Seven names: {}".format(usernames_test1))
    print()
    usernames_test2 = random_name_list(10)  # generates a list with 10 random names
    print(usernames_test2)
    usernames(usernames_test2)
    print("Ten names: {}".format(usernames_test2))
    print()

    print("Testing number_lines()")
    number_lines("nirvana.txt")
    print()
    number_lines("queen.txt")
    print()

    print("Testing models()")
    print("The average surface area of the spheres in the 'planets.txt'"
          " file is {:.2f}\n".format(models("planets.txt",
                                            "planets_surface.txt")))
    with open("planets_surface.txt", 'r') as output:
        print(output.read())


# Functions that generate random numbers and names for the testing cases
# I left them at the bottom because they are not part of the lab.
# In other circumstances I would leave it before the function test()
# because that's 'where' they are being used.
def random_name_lists():
    """This function splits a lits of full names into 3 lists:
    first, middle and last names"""

    names = ['Lily Jane Collins', 'Millie Bobby Brown',
             'Sacha Baron Cohen', 'Oliver Jackson Cohen',
             'Adam Douglas Driver', 'Joaquim Rafael Bottom',
             'Daisy Jazz Ridley', 'Carrie Frances Fisher',
             'Robert Downey Jr', 'Christopher Robert Evans',
             'Christopher Michael Pratt', 'Steven John Carell',
             'Margaret Constance Williams',
             'Christopher Catesby Harington', 'Sophie Belinda Jonas']

    first_names = []
    middle_names = []
    last_names = []

    for i in range(len(names)):
        full_name = names[i]
        list_name = full_name.split()
        first_names.append(list_name[0])
        middle_names.append(list_name[1])
        last_names.append(list_name[-1])
    return first_names, middle_names, last_names


def random_name():
    """This function mix and match the names entered in
    random_name_lists() to create random names"""

    first_names, middle_names, last_names = random_name_lists()

    full_name = random.choice(first_names) + " " + \
                random.choice(middle_names) + " " + \
                random.choice(last_names)

    return full_name


def random_name_list(number_names):
    """This function uses random_name() to create a list of random names"""

    random_names = []
    for i in range(number_names):
        random_names.append(random_name())

    return random_names


def random_numbers(n):
    """This function generates a list of random integers and floats"""

    number_list = []
    for i in range((n // 2)):
        rand_float = random.uniform(0.0, 10.0)
        rand_int = random.randint(0, 10)
        number_list.append(rand_float)
        number_list.append(rand_int)
    return number_list


def random_numbers_str(n):
    """This function converts a list of numbers into a list of strings"""

    number_list = random_numbers(n)
    for i in range(len(number_list)):
        number = str(number_list[i])
        number_list[i] = number

    return number_list


test()
