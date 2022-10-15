#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
def minimumBribes(q):
    n1 = 1
    n2 = 2
    n3 = 3
    total = 0
    
    for i in q:
        if i == n1:
            n1, n2, n3 = n2, n3, n3 + 1
        elif i == n2:
            total += 1
            n2, n3 = n3, n3 + 1
        elif i == n3:
            total += 2
            n3 += 1
        else:
            print("Too chaotic")
            return
    print(total)       
                

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)