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
    return      # you will need to add a return value

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
    assert calcTax(34.75,0.12) == 4.17
    assert calcTax(43.6,0.03) == 1.31
    assert calcTax(49.01,0.04) == 1.96
    assert calcTax(80.63,0.07) == 5.64
    assert calcTax(4.78,0.03) == 0.14
    assert calcTax(83.52,0.1) == 8.35
    assert calcTax(103.91,0.12) == 12.47
    assert calcTax(116.57,0.09) == 10.49
    assert calcTax(78.39,0.11) == 8.62
    assert calcTax(129.2,0.1) == 12.92
    assert calcTax(19.09,0.03) == 0.57
    assert calcTax(12.5,0.04) == 0.5
    assert calcTax(47.49,0.04) == 1.9
    assert calcTax(102.94,0.04) == 4.12
    assert calcTax(16.58,0.05) == 0.83
    assert calcTax(56.48,0.07) == 3.95
    assert calcTax(148.14,0.07) == 10.37
    assert calcTax(9.63,0.1) == 0.96
    assert calcTax(94.01,0.11) == 10.34
    assert calcTax(8.23,0.12) == 0.99  
 