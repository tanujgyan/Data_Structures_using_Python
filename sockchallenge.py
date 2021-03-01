#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    numberOfPairs=0
    for x in ar:
        #count the number of pairs of the element
        numberOfPairs = numberOfPairs+ (ar.count(x)//2)
        #remove the element which was counted
        ar=list(filter((x).__ne__, ar)) 
    return numberOfPairs

if  __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout 
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()