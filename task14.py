#!python3
# Find the tax

"""
Different provinces charge different amounts of sales tax

Write a program that takes 1 required positional argument (price)
and 1 optional argument: percent
We will use a default value of 7% sales tax for BC
"""

import random
def calcTax():  # you will need to add your arguments here
    return     # you will need to add a return value

if __name__ == "__main__":
    assert calcTax(61.49) == 4.3
    assert calcTax(121.71) == 8.52
    assert calcTax(106.83) == 7.48
    assert calcTax(101.66) == 7.12
    assert calcTax(125.12) == 8.76
    assert calcTax(141.78) == 9.92
    assert calcTax(23.23) == 1.63
    assert calcTax(94.61) == 6.62
    assert calcTax(44.85) == 3.14
    assert calcTax(145.52) == 10.19
    assert calcTax(42.7) == 2.99
    assert calcTax(125.67) == 8.8
    assert calcTax(40.33) == 2.82
    assert calcTax(55.25,3) == 3.87
    assert calcTax(67.51,12) == 4.73
    assert calcTax(148.98,12) == 10.43
    assert calcTax(84.57,6) == 5.92
    assert calcTax(37.07,6) == 2.59
    assert calcTax(103.21,3) == 7.22
    assert calcTax(122.61,4) == 8.58
    assert calcTax(108.74,7) == 7.61
    assert calcTax(20.2,10) == 1.41
    assert calcTax(122.75,6) == 8.59
    assert calcTax(37.33,6) == 2.61
    assert calcTax(123.69,12) == 8.66
    assert calcTax(114.37,4) == 8.01
    assert calcTax(61.29,8) == 4.29
    assert calcTax(4.35,4) == 0.3
    assert calcTax(6.23,6) == 0.44
    assert calcTax(121.29,6) == 8.49
    assert calcTax(115.64,6) == 8.09
    assert calcTax(84.35,9) == 5.9    