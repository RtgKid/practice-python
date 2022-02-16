# Problem
# Note: The main parts of the statements of the problems "Reversort" and "Reversort Engineering" are identical, except for the last paragraph. The problems can otherwise be solved independently.

# Reversort is an algorithm to sort a list of distinct integers in increasing order. The algorithm is based on the "Reverse" operation. Each application of this operation reverses the order of some contiguous part of the list.

# The pseudocode of the algorithm is the following:

# Reversort(L):
#   for i := 1 to length(L) - 1
#     j := position with the minimum value in L between i and length(L), inclusive
#     Reverse(L[i..j])
# After i−1 iterations, the positions 1,2,…,i−1 of the list contain the i−1 smallest elements of L, in increasing order. During the i-th iteration, the process reverses the sublist going from the i-th position to the current position of the i-th minimum element. That makes the i-th minimum element end up in the i-th position.

# For example, for a list with 4 elements, the algorithm would perform 3 iterations. Here is how it would process L=[4,2,1,3]:

# i=1, j=3⟶L=[1,2,4,3]
# i=2, j=2⟶L=[1,2,4,3]
# i=3, j=4⟶L=[1,2,3,4]
# The most expensive part of executing the algorithm on our architecture is the Reverse operation. Therefore, our measure for the cost of each iteration is simply the length of the sublist passed to Reverse, that is, the value j−i+1. The cost of the whole algorithm is the sum of the costs of each iteration.

def reversort(l):
    counter = 0
    for i in range(0, len(l) - 1):
        j = l.index(min(l[i:len(l)]))
        counter += len(l[i:j+1])

        temp = l[i:j+1]
        temp.reverse()
        l[i:j+1] = temp
    return counter

n = int(input())
for i in range(n):
    m = input()
    line = input()
    l = [int(i) for i in line.split()]
    print("Case #" + str(i+1) + ": " + str(reversort(l)))