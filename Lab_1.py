############################################################
# Name: Sandya Devanahally
# Pledge: I pledge my honor that I have abided by the Stevens Honor System 
# CS115 Lab 1
#
############################################################

from math import factorial
from functools import reduce
def inverse(x):
    '''Returns the inverse of any number x'''
    return 1.0/x
def e(n):
    '''numbers_list creates a list with 1 to n
      fact_list computes the factorial of the numbers in number_list
      inv_list takes the inverse of all the numbers in fact_list
      returns the sum of all the numbers in inv_list'''
    numbers_list = list(range(n+1))
    fact_list = list(map(factorial, numbers_list))
    inv_list = list(map(inverse,fact_list))
    return reduce(sum, inv_list)
def sum(x,y):
    '''Returns the sum of x & y'''
    return (x+y)

#brain dump #1
#ok so first you are given a number x
#multiply the number by 1/n
#return inverse 


#brain dump #2
#basically youre given a number n
#need make a list from range 1, n+1
#and then apply a function to that list that does the factorial of the inverse
#and add all those numbers
#return the sum
