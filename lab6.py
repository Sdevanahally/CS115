'''
Created on 10/19/2023
@author:   Sandya Devanahally
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2 ==0:
        return False
    else:
        return True

#42 in base 2 -- 101010
#if it is an odd base-10 number then it will be a 1as the right-most bit.
#If it is an even base- 10 number then it will be a 0 as the right-most bit.
#if you delete the right-most bit, then you essentially divide the number by 2
#if n is even, you would add 0 as the right-most bit. if n is odd, you would add 1 as the right-most bit.
    
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n ==0:
        return '' #base case
    elif isOdd(n):
        return numToBinary(n//2) + '1' #odd
    else:
        return numToBinary(n//2) + '0' #even

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if len(s) == 0:
        return 0
    else:
        return binaryToNum(s[:-1]) * 2 + int(s[-1])
    

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ('00000000' + numToBinary(binaryToNum(s) + 1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n>0:
        print(s)
        return count(increment(s), n-1)
    else:
        print(s)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if (n==0):
        return ''
    else:
        return numToTernary(n//3) + str(n%3)
    

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if (s == ''):
        return 0
    else:
        return ternaryToNum(s[:-1]) * 3 + int(s[-1])
