# mandelbrot.py
# Lab 9
#
# Name: Sandya Devanahally
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

#mult function
def mult(c, n):
    """ mult uses only a loop and addition to multiply c by the integer n """
    result = 0
    for item in range(n):
        result += c
    return result

#update function
def update(c, n):
    """ update starts with z=0 and runs z = z**2 + c for a total of n times. It returns the final z."""
    z = 0
    for item in range(n):
        z = z **2 + c
    return z

#inMSet funciton
def inMSet(c, n):
    """ inMSet takes in c for the update step of z = z**2+c
       n, the maximum number of times to run that step
       Then, it should return False as soon as abs(z) gets larger than 2 andTrue if abs(z) never gets larger than 2 (for n iterations)"""
    z = 0
    for item in range(n):
        z = z **2 + c
        if (abs(z) > 2):
            return False
    return True

#images
def weWantThisPixel( col, row ):
    """ a function that returns True if we want the pixel at col, row and False otherwise """
    if col%10 == 0 and row%10 == 0:
        return True
    else:
        return False

def test():
    """ a function to demonstrate how to create and save a png image"""
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    image.saveFile()

 #scale and mset
def scale(pix, pixMax, floatMin, floatMax):
    '''This function takes four inputs and returns the corresponding place of the pixel'''
    tempRange = floatMax - floatMin
    temp = (pix/pixMax) * tempRange + floatMin
    return temp

def mset():
    '''This function creats a fractal using the values that make the mset true'''
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            x = scale(col, width, -2, 1)
            y = scale(row, height, -1, 1)
            c = x + y*1j
            n = 25
            if inMSet(c, n) == True:
                image.plotPoint(col, row)
    image.saveFile()



    
