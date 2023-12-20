'''
Created on 10/21/2023
@author:   Sandya Devanahally
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
from functools import reduce
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


#HELPER FUNCTIONS

def count(s):
    '''Takes string s and returns list of all consecutive counts of the same digit'''
    if s == '':
        return 0
    if len(s) == 1:
        return 1
    if s[0] == s[1]:
        return 1 + count(s[1:])
    else:
        return 1

def countList(s):
    '''Takes input s and returns a list of all of the digits '''
    if s == '':
        return []
    return [count(s)] + countList(s[count(s):])

def split(l):
    '''Splits input list l into lengths of size MAX_RUN_LENGTH'''
    if l == []:
        return []
    if l[0] > MAX_RUN_LENGTH:
        l[0] = l[0] - MAX_RUN_LENGTH
        return [MAX_RUN_LENGTH, 0] + split(l)
    return [l[0]] + split(l[1:])

def isOdd(n):
    '''Determines if a number is odd'''
    return n % 2 == 1

def numToBinary(n):
    """converts a decimal number to a binary string"""
    if n==0:
        return ""
    else:
        if isOdd(n):
            ans = numToBinary(n//2) + "1"
            return ans
        else:
            ans = numToBinary(n//2) + "0"
            return ans

def fill(n):
    '''Fills in 0's in empty spaces before number'''
    if (len(n) < COMPRESSED_BLOCK_SIZE):
        return '0' * (COMPRESSED_BLOCK_SIZE - len(n)) + n
    return n

def binaryToNum(s):
    """converts binary string s to decimal number"""
    n = len(s)
    if s=="":
        return 0
    else:
        ans = int(s[0])*(2**(n-1)) + binaryToNum(s[1:])
        return ans

def add(x, y):
    '''This function returns the sum of two numbers'''
    return x + y

#Compression

def compress(s):
    '''Takes input s and returns compression of the binary string'''
    if s[0] == '1':
        binaryList = list(map(numToBinary, split(countList(s))))
        fillList = (list(map(fill, binaryList)))
        mult = reduce(add, fillList)
        return '0' * COMPRESSED_BLOCK_SIZE + mult
    binaryList = list(map(numToBinary, split(countList(s))))
    fillList = list(map(fill, binaryList))
    return reduce(add, fillList)

#uncompress
def uncompress(s):
    '''Takes binary string s and returns the uncompressed version based on the COMPRESSED_BLOCK_SIZE'''
    def uncompress1(s, c):
        if (s == ''):
            return ''
        if (c % 2 == 0):
            return '0'* binaryToNum(s[:COMPRESSED_BLOCK_SIZE]) + uncompress1(s[COMPRESSED_BLOCK_SIZE:], c + 1)
        return '1' * binaryToNum(s[:COMPRESSED_BLOCK_SIZE]) + uncompress1(s[COMPRESSED_BLOCK_SIZE:], c + 1)
    return uncompress1(s, 0)

#compression
def compression(n):
    '''Returns ratio of the compression size to original size'''
    return len(compress(n)) / len(n)
