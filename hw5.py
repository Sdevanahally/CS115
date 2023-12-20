'''
Created on 10/13/2023
@author:   Sandya Devanahally
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 
'''

memo = { }
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in memo:
        return memo[n]
    if n == 0: #base case - the list is empty - return 2
        memo[n] = 2
        return 2
    elif n == 1:
        memo[n] = 1
        return 1
    else:#recursibe step 
        ans = fast_lucas(n-1) + fast_lucas(n-2)
        memo[n] = ans
        return ans

memo2= { }
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if (amount, tuple(coins)) in memo2:
        return memo2[(amount, tuple(coins))]
    elif amount == 0:
        memo2[(amount, tuple(coins))] = 0
        return 0
    elif coins == [] or amount < 0:
        memo2[(amount, tuple(coins))] = float("inf")
        return float("inf")
    elif coins[0] > amount:
        answer = fast_change(amount, coins[:-1])
        memo2[(amount, tuple(coins))] = answer
        return answer
    else:
        useIt = 1 + fast_change(amount - coins[0], coins)
        loseIt = fast_change(amount, coins[1:])
        answer = min(useIt, loseIt)
        memo2[(amount, tuple(coins))] = answer
        return answer
# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


