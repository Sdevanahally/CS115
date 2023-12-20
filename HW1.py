#Sandya Devanahally
#I pledge my honor that I have abided by the Stevens Honor System.
#CS115 Homework 1

from math import factorial
from functools import reduce

def multiply(x,y):
    """Returns the product of x and y"""
    return x*y

def factorial(n):
    """takes a positive integer n and returns n!"""
    numbers = range(1, n+1)
    return reduce(multiply, numbers)

def add(x, y):
    """returns the sum of two numbers"""
    return x+y

def mean(L):
    """takes a list as input and returns the mean (average) value in that list."""
    total = reduce(add, L)
    return total/len(L)
