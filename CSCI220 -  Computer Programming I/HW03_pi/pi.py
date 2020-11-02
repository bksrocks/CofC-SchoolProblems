# Name: Barbara Szwabowski
# pi.py

# Purpose: Compute the number of pi using the Wallis product, the
# Gregory-Leibniz series, the Nilakantha Series and the Euler’s method,
# then see how those results compare to math.pi

# Certification of Authenticity: I certify that this lab is entirely my
# own work.

# Input: The number of terms to the approximation

# Output: The calculated pi and the approximation error for each of the
# calculations


import math


def pi_wallis(n):
    print("This function approximates the value of pi using the Wallis "
          "product.")
    wallis = 1
    # this loop calculates the number of pi using the Wallis product
    # with the approximation index defined by user input
    # 𝜋/2 = 2/1 ∗ 2/3 ∗ 4/3 ∗ 4/5 ∗ 6/5 ∗ 6/7 ∗ 8/7 ∗ ...
    for i in range(n):
        numerator = (2 * (i//2)) + 2
        denominator = (2 * ((i - 1) // 2)) + 3
        wallis *= (numerator/denominator)
    wallis = wallis * 2
    # total compares the result obtained in the calculations with the
    # value of pi in the math library.
    total = math.pi - wallis
    # outputs the results
    print("By the Wallis product, with a", n, "approximation , pi "
                                              "equals:", wallis)
    print("The approximation error of the Wallis product is:", total)
    print()


def pi_gregory(n):
    print("This function approximates the value of pi by adding the "
          "terms of the Gregory-Leibniz series")
    gregory = 0
    # this loop calculates the number of pi using the Gregory-Leibniz
    # series with the approximation index defined by user input
    # 4/1 − 4/3 + 4/5 − 4/7 + 4/9 − 4/11 + ...
    for i in range(n):
        numerator = 4 * ((-1) ** i)
        denominator = (2 * i) + 1
        gregory += (numerator/denominator)
    total = math.pi - gregory
    # outputs the results
    print("By the Gregory-Leibniz series, with a", n, "approximation, "
            "pi equals:", gregory)
    print("The approximation error of the Gregory-Leibniz series is:",
          total)
    print()


def pi_nilakantha(n):
    print("This funcition approximates the value of pi using the "
          "Nilakantha series")
    # initiates the variable with value 3, according to the Nilakantha
    # series.
    nilakantha = 3
    # this loop calculates the number of pi using the Nilakantha
    # series with the approximation index defined by user input
    #  3 + 4/(2∗3∗4) − 4/(4∗5∗6) + 4/ (6∗7∗8) − 4/(8∗9∗10) +
    #  4/(10∗11∗12) − 4/ (12∗13∗14) + ...
    for i in range(n):
        numerator = 4 * ((-1) ** i)
        med = ((2 * i) + 3)
        denominator = (med-1) * med * (med+1)
        nilakantha += (numerator/denominator)
    total = math.pi - nilakantha
    # outputs the results
    print("By the Nilakantha series, with a", n, "approximation, pi "
                                                 "equals:", nilakantha)
    print("The approximation error of the Nilakantha series is:", total)
    print()


def pi_euler(n):
    print("This function approximates the value of pi using Euler’s "
          "method when Leonhard Euler solved the Basel problem")
    euler = 0
    # this loop calculates the number of pi using the Euler method with
    # the approximation index defined by user input
    # 𝜋^2/6 = 1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ...
    for i in range(1, n):
        numerator = 1
        denominator = i ** 2
        euler += (numerator/denominator)
    euler = (euler * 6) ** 0.5
    total = math.pi - euler
    # outputs the results
    print("By the Euler's method, with a", n, "approximation, pi "
                                                 "equals:", euler)
    print("The approximation error of the Euler's method is:", total)
    print()


def main():
    approx_num = eval(input("Enter the number of therms to calculate "
                            "the approximation: "))
    pi_wallis(approx_num)
    pi_gregory(approx_num)
    pi_nilakantha(approx_num)
    pi_euler(approx_num)


main()
