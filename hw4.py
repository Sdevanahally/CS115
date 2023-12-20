###############################################################
# Name: Sandya Devanahally
# I pledge my honor that I have abided by the Stevens Honor System.
# HW 4
###############################################################

#Task 1

def pascal_row(n):
    '''takes n as an input and returns corresponding row of pascal's triangle'''
    if n == 0:#base case - list is empty
        return [1]
    elif n == 1:
        return [1, 1]
    else: #base case
        return [1] + helper(pascal_row(n - 1))

def helper(l):
    '''This function takes in an input and return corresponding list of values'''
    if l == []:#base case empty list
        return []
    if len(l) == 1:
        return [1]#recursive step
    else:
        return [l[0] + l[1]] + helper(l[1:])

#Task 2

def pascal_triangle(n):
    '''takes input n and returns pascal triangle w/ n rows'''
    if n == 0: #base case
        return [[1]]
    elif n == 1:
        return [[1], [1, 1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

#Task 3
def test_pascal_row():
    '''This function tests the pascal row function'''
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]

def test_pascal_triangle():
    '''This function tests the pascal triangle function'''
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
