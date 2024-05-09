#!python3
# Find the tax

"""
Different provinces charge different amounts of sales tax

Write a program that takes 1 required positional argument (price)
and 1 optional argument: percent
We will use a default value of 7% sales tax for BC
"""

import random
def calcTax(p,r=0.07):  # you will need to add your arguments here
    return round(p*r,2)     # you will need to add a return value

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
    assert calcTax(145.85,6) == 875.1
    assert calcTax(133.12,8) == 1064.96 
    assert calcTax(65.99,11) == 725.89  
    assert calcTax(95.97,6) == 575.82   
    assert calcTax(128.9,11) == 1417.9  
    assert calcTax(116.55,7) == 815.85  
    assert calcTax(101.05,9) == 909.45  
    assert calcTax(57.46,7) == 402.22   
    assert calcTax(93.29,5) == 466.45   
    assert calcTax(104.64,11) == 1151.04
    assert calcTax(120.75,6) == 724.5   
    assert calcTax(123.91,12) == 1486.92
    assert calcTax(65.58,11) == 721.38
    assert calcTax(82.75,12) == 993.0
    assert calcTax(71.6,5) == 358.0
    assert calcTax(41.55,3) == 124.65
    assert calcTax(66.43,8) == 531.44
    assert calcTax(36.75,11) == 404.25
    assert calcTax(110.69,4) == 442.76
    assert calcTax(48.13,11) == 529.43   
 