#####################################################
#Sandya Devanahally
#I pledge my honor that I have abided by the Stevens Honor System
#####################################################

#length 
def length(l):
    """In the base case, the length is zero, so the length is returned as zero"""
    if l==[] or l==" ":
        return 0
    return 1+ length(l[1:])
    
#dot program
def dot(L, K):
    """In the base case, the vector is empty, so the dot product is returned as zero"""
    if L==[] and K==[]:
        return 0
    """In the recursive step, it calculates the dot product of the vectors then calls the recursive function on the sliced lists"""
    return (L[0]* K[0]) + dot(L[1:], K[1:])

#explode program
def explode(S):
    """In the base case, the string is empty, so an empty list is returned"""
    if S=="":
        return []
    """In the recursive step, returns a list of the characters (each of which is a string of length 1) in that string """
    return [S[0]] + explode(S[1:])

#ind program
def ind(e, L):
    """In the base case, it checks if e is not in L and returns an empty string
    In the recursive step, it returns the index at which e is first found in L"""
    if e not in L:
        return len(L)
    if L == [] or L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

#removeAll program
def removeAll(e, L):
    """In the base case, the list is empty, so an empty list is returned
    In the recursive step it removes all of the values in L that are equal to e"""
    if L==[]:
        return[]
    elif L[0]==e:
        return [] + removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

#myFilter program
def myFilter(function, L):
    """In the base case it checks if the list is empty and returns an empty list if that is true
    In the recursive step the function applies the function to everything in the list """
    if L==[]:
        return []
    elif function(L[0]):
        return [L[0]] + myFilter(function, L[1:])
    else:
        return myFilter(function, L[1:])
     

#deepReverse program
def deepReverse(L):
    """In the base case if L doesnt satisfy the parameters it returns an empty list
    In the recursive step it reverses every item in the list testing whether or not an element in the list is a list itself"""
    if not L:
        return []
    elif isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    else:
        return [L[-1]] + deepReverse(L[:-1])

    

        


