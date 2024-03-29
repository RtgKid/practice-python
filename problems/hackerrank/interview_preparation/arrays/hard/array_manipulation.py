import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    s = c = 0
    n = [0] * (n+1)
    for a, b, k in queries:
        n[a-1] += k
        n[b] -= k
    for i in n:
        c += i
        if c > s:
            s = c    
    return s    

def arrayManipulation1(n, queries):
    m = 0
    for i in range(1, n+1):
        s = 0
        for a,b,k in queries:
            if a <= i and i <= b:
                s+=k
        if s > m:
            m = s        
    return m    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
