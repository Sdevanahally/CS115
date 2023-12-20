####################################################################
# Name: Sandya Devanahally
# I pledge my honor that I have abided by the Stevens Honor System.
# Lab 3
####################################################################

def change(amount, coins):
    """ Given an amount of money and a list of coin types, finds the least
number of coins that makes up that amount of money."""
    if amount <= 0:
        return 0
    if coins ==[]:
        return float("inf")
    if len(coins) == 1:
        return 1+ change(amount - 1, coins)
    elif coins[len(coins)-1] > amount:
        return change(amount, coins[:-1])
    else:
        useIt = 1 + change(amount- coins[len(coins)-1], coins)
        loseIt = change(amount, coins[:-1])
        return min(useIt, loseIt)


#amount is a non-negative int indicating the amt of money to be made
#coins is a list of coin values - 1 is always in the list
#returns  non-negative integer indicating the minimum number of coins required to make up the gven amount.
# if no solution -- return infinity
