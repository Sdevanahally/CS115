'''
Created on Monday, September 25th, 2023
@author: Sandya Devanahally & Arushi Kashyap
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
sys.setrecursionlimit(10000)


# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    """base case: the scorelist is empty - recursive step finds the score of any letter given a scorelist"""
    if scorelist =="":
        return 0
    if scorelist[0][0] == letter:
        return scorelist [0][1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    """returns the score of a word"""
    if S== "":
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:],  scorelist)

def checkWord(rack):
    """Takes input rack and returns if a word is possible"""
    def test(S):
        """checks if a letter from the rack exists in the word"""
        if S == '':
            return True
        elif type(S) == str:
            S = list(S)
        elif S == []:
            return True
        elif rack == []:
            return False

        if rack[0] in S:
            S.remove(rack[0])
            return checkWord(rack[1:])(S)
        return checkWord(rack[1:])(S)
    return test

def return_scores(l):
    """takes an input list and returns the list of scores"""
    if l == []:
        return []
    word = l[0]
    score = wordScore(word, scrabbleScores)
    rest_scores = return_scores(l[1:])
    
    return [[word, score]] + rest_scores

def scoreList(rack):
    """Takes input rack and returns the list of all words and scores possible"""
    filtered_list = list(filter(checkWord(rack), Dictionary))
    word_scores = [[word, wordScore(word, scrabbleScores)] for word in filtered_list]    
    return word_scores


def bestWord(rack):
    """returns the best word possible given a rack"""
    def find_best(words, best, current):
        if not words:
            return best
        word, score = words[0]
        if score > current[1]:
            return find_best(words[1:], [word, score], [word, score])
        else:
            return find_best(words[1:], best, current)

    words_with_scores = scoreList(rack)
    if not words_with_scores:
        return ["", 0]
    
    return find_best(words_with_scores, words_with_scores[0], words_with_scores[0])
