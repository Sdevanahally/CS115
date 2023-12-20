#################################################################
#Name: Sandya Devanahally
#Pledge: I pledge my honor that I have abided by the Stevens honor system.
# Lab 4
##################################################################

def knapsack(capacity, itemList):
    """returns both the max value and the list of items that make this value without exceeding thr capacity of the knappsack"""
    if capacity <= 0: #base case - the capacity is zero or the list is empty
        return [0, []]
    elif itemList == []:
        return [0, []]
    elif itemList[0][0] > capacity: #recursive step if the first item in the list is bigger than capacity
        return knapsack(capacity, itemList[1:])
    else: #use it or lose it strategy
        use_it = knapsack(capacity - itemList[0][0], itemList[1:])
        lose_it = knapsack(capacity, itemList[1:])

        if lose_it[0] < itemList[0][1] + use_it[0]: #list of items with max value
            return [itemList[0][1] + use_it[0]] + [[itemList[0]] + use_it[1]]
        else:
            return [lose_it[0]] + [lose_it[1]]
            
