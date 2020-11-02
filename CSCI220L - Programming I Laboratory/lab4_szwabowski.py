# Name: Barbara Szwabowski
# lab4_szwabowski.py
# Purpose: Lab 4 assignments

from graphics import *


def patterns():
	print("Generates the first n elements of several patterns.")
	num_elements = int(input("How many elements do you want to see? "))
	functions = [pattern_a, pattern_b, pattern_c, pattern_d, pattern_e]
	for func in functions:
		func(num_elements)


def pattern_a(n):
	# Output: 2 4 6 8 10
	print("Pattern A: ", end='')
	for i in range(n):
		print(2 * i + 2, end=' ')
	print()


def pattern_b(n):
	# Output: 1+4+7+10+13
	print("Pattern B: ", end='')
	for i in range(n):
		print((3 * i + 1), end=' ')
	print()


def pattern_c(n):
	# Output: 0 6 0 6 0 6
	print("Pattern C: ", end='')
	for i in range(n):
		print((i % 2) * 6, end=' ')
	print()


def pattern_d(n):
	# Output: 2−4+4−4+6−6+6−8
	print("Pattern D: ", end='')
	pattern_sum = 0
	for i in range(n):
		pattern = ((2 * ((i + 2) // 3)) * (-1) ** i)
		pattern_sum += pattern
	print(pattern_sum)


def pattern_e(n):
	# Output: 3/2∗5/4∗7/8∗9/16∗11/32
	print("Pattern E: ", end='')
	pattern_total = 1
	for i in range(n):
		numer = (i * 2) + 3
		denom = 2 ** (i + 1)
		pattern_total *= (numer / denom)
	print(round(pattern_total, 2))


def hw_stats():
	print("This function calculates the mean and standard deviation of "
		  "a student's grades")

	number_assignment = eval(input("Enter the number of assignments: "))
	total_grades, accum, st_deviation = 0, 0, 0
	grades = []

	# This loop adds the grades to a list and also calculates de mean
	# of the grades entered by the user
	for i in range(number_assignment):
		grade = eval(
			input("Enter your grade on HW" + str(i + 1) + ": "))
		grades.append(grade)
		total_grades += grade
	mean = total_grades / number_assignment

	# This lop does part of the calculation for standard deviation
	for j in range(number_assignment):
		accum += ((grades[j] - mean) ** 2)
	# Final calculation of the standard deviation
	st_deviation = (((1 / number_assignment) * accum) ** (1 / 2))

	# Outputs the result of the calculations
	print("Your overall average is", round(mean, 1))
	print("The standard deviation is", round(st_deviation, 2))


def draw_shapes():
	# how many times the user can move the circle
	NUM_CLICKS = 5

	# create the window
	width = 800
	height = 400
	win = GraphWin("Drawing Shapes", width, height)

	# display instructions
	instr_pt = Point(width / 2, height - 10)
	# instructions = Text(instr_pt, "Click to move circle")
	instructions = Text(instr_pt, "Click to move rectangle")
	instructions.draw(win)

	# build the //circle// rectangle
	# shape = Circle(Point(50, 50), 20)
	shape = Rectangle(Point(30, 30), Point(50, 50))
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)

	# allow the user to click multiple times
	for i in range(NUM_CLICKS):
		pt = win.getMouse()
		center = shape.getCenter()

		# move amount is the distance from center to the click point
		dx = pt.getX() - center.getX()
		dy = pt.getY() - center.getY()
		shape.move(dx, dy)

	# clean up
	instructions.setText("Click again to close")
	win.getMouse()
	win.close()


def main():
	pass
	# patterns()
	# pattern_b(8)
	# hw_stats()
	# draw_shapes()


main()
